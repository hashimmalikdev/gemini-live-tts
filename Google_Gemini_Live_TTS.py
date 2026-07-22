"""
Requirements: pip install google-genai pyaudio python-dotenv
"""

import os
import asyncio
import queue
import time
import sys
import threading

import pyaudio
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Global low-latency audio structures
FORMAT = pyaudio.paInt16
CHANNELS = 1
RECEIVE_SAMPLE_RATE = 24000
MODEL = "models/gemini-3.1-flash-live-preview"

_main_loop = None
_input_queue = None
_output_queue = queue.Queue()
_playback_queue = queue.Queue()
_bg_thread = None


def _global_playback_worker():
    """
    Background Audio Worker: Continually reads raw audio chunks from the queue 
    and sends them to PyAudio to play sound through your speakers with zero delay.
    """
    pya = pyaudio.PyAudio()
    try:
        stream = pya.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RECEIVE_SAMPLE_RATE,
            output=True,
            frames_per_buffer=1024
        )
        while True:
            chunks = []
            while not _playback_queue.empty():
                try:
                    chunks.append(_playback_queue.get_nowait())
                except queue.Empty:
                    break
            
            if chunks:
                stream.write(b"".join(chunks))
                for _ in range(len(chunks)):
                    _playback_queue.task_done()
            else:
                time.sleep(0.001)
    except Exception:
        pass


class AudioLoop:
    def __init__(self):
        """
        Constructor: Sets up session variables, completion signals, 
        and text buffers needed to track Gemini's response.
        """
        self.session = None
        self.gemini_finished = asyncio.Event()
        self.all_responses = []
        self.current_turn_text = ""

    async def receive_audio(self):
        """
        Live Stream Listener: Asynchronously processes data coming back from Gemini. 
        It streams text to the terminal live and pushes raw audio straight to the playback queue.
        """
        while True:
            if self.session is not None:
                async for response in self.session.receive():
                    if response.server_content:
                        # Output text streaming
                        if response.server_content.output_transcription:
                            chunk_text = response.server_content.output_transcription.text
                            sys.stdout.write(chunk_text)
                            sys.stdout.flush()
                            self.current_turn_text += chunk_text
                        
                        # Handle turn completion
                        if response.server_content.turn_complete:
                            if self.current_turn_text:
                                self.all_responses.append(self.current_turn_text)
                                self.current_turn_text = ""
                            self.gemini_finished.set()
                        
                        # Audio chunk streaming to PyAudio queue
                        if response.server_content.model_turn:
                            for part in response.server_content.model_turn.parts:
                                if part.inline_data and part.inline_data.data:
                                    _playback_queue.put(part.inline_data.data)


async def background_async_loop():
    """
    Async Engine Manager: Runs the background event loop, maintains the active 
    Gemini WebSocket connection, manages input prompts, and clears leftover audio.
    """
    global _input_queue, _main_loop
    _main_loop = asyncio.get_running_loop()
    _input_queue = asyncio.Queue()
    
    client = genai.Client(
        http_options={"api_version": "v1beta"},
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    
    current_voice = "Zephyr"
    threading.Thread(target=_global_playback_worker, daemon=True).start()
    
    while True:
        CONFIG = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            output_audio_transcription=types.AudioTranscriptionConfig(),
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=current_voice)
                )
            ),
        )
        
        loop_instance = AudioLoop()
        
        try:
            async with (
                client.aio.live.connect(model=MODEL, config=CONFIG) as session,
                asyncio.TaskGroup() as tg,
            ):
                loop_instance.session = session
                tg.create_task(loop_instance.receive_audio())
                
                while True:
                    item = await _input_queue.get()
                    next_query, next_voice = item
                    
                    if next_voice != current_voice:
                        current_voice = next_voice
                        await _input_queue.put(item)
                        raise Exception("Reconnecting to update voice config")
                        
                    # Flush lingering audio before new request
                    while not _playback_queue.empty():
                        try:
                            _playback_queue.get_nowait()
                            _playback_queue.task_done()
                        except queue.Empty:
                            break
                            
                    loop_instance.gemini_finished.clear()
                    await loop_instance.session.send_realtime_input(text=next_query or ".")
                    await loop_instance.gemini_finished.wait()
                    
                    _output_queue.put(loop_instance.all_responses[-1] if loop_instance.all_responses else "")
                    _input_queue.task_done()
                    
        except Exception:
            await asyncio.sleep(0.1)


def start_background_thread():
    """
    Thread Launcher: Initializes a separate thread dedicated to running 
    the asyncio event loop so the main program doesn't freeze or lock up.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(background_async_loop())


def TTS(query, voice="Zephyr"):
    """
    Text-To-Speech Interface: Prepares the prompt for repetition, sends it to 
    the background thread, and clears live streaming output after execution.
    """
    formatted_query = f"Repeat the following text exactly. Output nothing else:\n{query}"

    global _bg_thread, _main_loop, _input_queue
    if _bg_thread is None:
        _bg_thread = threading.Thread(target=start_background_thread, daemon=True)
        _bg_thread.start()
        while _main_loop is None or _input_queue is None:
            time.sleep(0.01)
        
    _main_loop.call_soon_threadsafe(_input_queue.put_nowait, (formatted_query, voice))
    final_response = _output_queue.get()
    
    if final_response:
        lines_to_clear = len(final_response.splitlines()) if final_response else 1
        sys.stdout.write("\r\033[K")
        for _ in range(lines_to_clear - 1):
            sys.stdout.write("\033[A\033[K")
        sys.stdout.write("\r\033[J")
        sys.stdout.flush()

    return final_response


if __name__ == '__main__':
    while True:
        query = input("\nQuery: ")
        output = TTS(query, "Zephyr")
        print(f"Final Return: {output}")
