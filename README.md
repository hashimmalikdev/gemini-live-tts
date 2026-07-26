# 🎙️ Gemini Live Unlimited Free TTS

A Python tool to convert text to speech **100% free and without limits** using Google's Gemini AI. Say goodbye to expensive TTS API subscriptions!

## 🎥 Video Demo

<p align="center">
  <a href="https://www.youtube.com/watch?v=xnbEBUnjChQ">
    <img src="https://img.youtube.com/vi/xnbEBUnjChQ/maxresdefault.jpg" alt="Build an Unlimited Free AI Voice Generator in Python" width="100%">
  </a>
</p>

---

## ✨ Features

- ♾️ **Unlimited & Free TTS:** Generate unlimited audio without high subscription costs.
- 🔊 **High-Quality Voice:** Converts text into clear, natural-sounding audio.
- ⚡ **Fast Performance:** Quick audio generation with streaming support.
- 💬 **Simple CLI:** Clean, easy-to-use terminal interface.

---

## 🗣️ Supported Voices

<details open>
<summary><b>Click to view all 30 Gemini Live preset voices</b></summary>

<br>

<table width="100%">
  <thead>
    <tr>
      <th align="left" width="20%">Voice Name</th>
      <th align="left" width="25%">Pitch Level</th>
      <th align="left" width="20%">Tone / Style</th>
      <th align="left" width="35%">Best For</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><b>Zephyr</b></td><td>🔊 Higher</td><td>Bright</td><td>Upbeat Announcements & Alerts</td></tr>
    <tr><td><b>Leda</b></td><td>🔊 Higher</td><td>Youthful</td><td>Gaming & Interactive Apps</td></tr>
    <tr><td><b>Laomedeia</b></td><td>🔊 Higher</td><td>Upbeat</td><td>Casual Conversation & Socials</td></tr>
    <tr><td><b>Achernar</b></td><td>🔊 Higher</td><td>Soft</td><td>Bedtime Stories & Relaxation</td></tr>
    <tr><td><b>Puck</b></td><td>🎙️ Middle</td><td>Upbeat</td><td>Virtual Assistants & Chatbots</td></tr>
    <tr><td><b>Kore</b></td><td>🎙️ Middle</td><td>Firm</td><td>Tutorials & Tech Documentation</td></tr>
    <tr><td><b>Aoede</b></td><td>🎙️ Middle</td><td>Breezy</td><td>Podcasts & Storytelling</td></tr>
    <tr><td><b>Callirrhoe</b></td><td>🎙️ Middle</td><td>Easy-going</td><td>Vlogs & Casual Explanations</td></tr>
    <tr><td><b>Autonoe</b></td><td>🎙️ Middle</td><td>Bright</td><td>Product Demos & Marketing</td></tr>
    <tr><td><b>Despina</b></td><td>🎙️ Middle</td><td>Smooth</td><td>Customer Service Bots</td></tr>
    <tr><td><b>Erinome</b></td><td>🎙️ Middle</td><td>Clear</td><td>Educational Content & E-Learning</td></tr>
    <tr><td><b>Rasalgethi</b></td><td>🎙️ Middle</td><td>Informative</td><td>News Updates & Reports</td></tr>
    <tr><td><b>Gacrux</b></td><td>🎙️ Middle</td><td>Mature</td><td>Business Presentations</td></tr>
    <tr><td><b>Pulcherrima</b></td><td>🎙️ Middle</td><td>Forward</td><td>Direct Instructions & Navigation</td></tr>
    <tr><td><b>Vindemiatrix</b></td><td>🎙️ Middle</td><td>Gentle</td><td>Guided Meditation & Wellness</td></tr>
    <tr><td><b>Sadaltager</b></td><td>🎙️ Middle</td><td>Knowledgeable</td><td>Audiobooks & Documentaries</td></tr>
    <tr><td><b>Sulafat</b></td><td>🎙️ Middle</td><td>Warm</td><td>Friendly Companion AI</td></tr>
    <tr><td><b>Fenrir</b></td><td>🎧 Lower Middle</td><td>Excitable</td><td>Gaming Commentary & Trailers</td></tr>
    <tr><td><b>Orus</b></td><td>🎧 Lower Middle</td><td>Firm</td><td>Security Announcements</td></tr>
    <tr><td><b>Iapetus</b></td><td>🎧 Lower Middle</td><td>Clear</td><td>Audio Guides & Explainer Videos</td></tr>
    <tr><td><b>Umbriel</b></td><td>🎧 Lower Middle</td><td>Easy-going</td><td>Late-night Radio & Chill Podcasts</td></tr>
    <tr><td><b>Alnilam</b></td><td>🎧 Lower Middle</td><td>Firm</td><td>Corporate Training Materials</td></tr>
    <tr><td><b>Schedar</b></td><td>🎧 Lower Middle</td><td>Even</td><td>Neutral Narration</td></tr>
    <tr><td><b>Achird</b></td><td>🎧 Lower Middle</td><td>Friendly</td><td>Onboarding Guides</td></tr>
    <tr><td><b>Zubenelgenubi</b></td><td>🎧 Lower Middle</td><td>Casual</td><td>Daily Updates & Notes</td></tr>
    <tr><td><b>Charon</b></td><td>🔉 Lower</td><td>Informative</td><td>Scientific & Historical Docs</td></tr>
    <tr><td><b>Enceladus</b></td><td>🔉 Lower</td><td>Breathy</td><td>Atmospheric Storytelling</td></tr>
    <tr><td><b>Algieba</b></td><td>🔉 Lower</td><td>Smooth</td><td>Professional Voiceover</td></tr>
    <tr><td><b>Algenib</b></td><td>🔉 Lower</td><td>Gravelly</td><td>Character Acting & Gaming</td></tr>
    <tr><td><b>Sadachbia</b></td><td>🔉 Lower</td><td>Lively</td><td>Dynamic Commercials</td></tr>
  </tbody>
</table>

</details>

---

## 📋 Prerequisites

- **Python 3.12.3** installed on your machine.
- A free **Google Gemini API Key** (Get it from [Google AI Studio](https://aistudio.google.com/)).

---

## 🚀 How to Use

Follow these simple steps to set up and run the project:

### Step 1: Clone the Repository
```bash
git clone https://github.com/hashimmalikdev/gemini-live-tts.git
cd gemini-live-tts
```

### Step 2: Create & Activate Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
pip install -r .\requirements.txt
```

### Step 4: Run TTS
```powershell
python Google_Gemini_Live_TTS.py
```
