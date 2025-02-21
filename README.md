# Personal Assistant Bot (Yuvi)

Yuvi is a voice-activated personal assistant powered by OpenAI's GPT and various APIs. It can perform tasks such as opening websites, playing music, fetching news, and answering general queries using AI.

## Features
- **Voice Recognition**: Uses `speech_recognition` to recognize voice commands.
- **Web Browsing**: Opens commonly used websites like Google, YouTube, LinkedIn, and GitHub.
- **Music Playback**: Plays songs from a predefined music library.
- **News Fetching**: Retrieves top news headlines using the NewsAPI.
- **AI Responses**: Uses OpenAI's GPT model to answer questions and assist with tasks.

## Prerequisites
Ensure you have Python installed (preferably Python 3.7 or later).

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies using pip:
   ```bash
   pip install speechrecognition pyttsx3 requests openai
   ```

## Required Libraries/Modules
- `speech_recognition`: For voice command recognition.
- `webbrowser`: To open websites.
- `pyttsx3`: For text-to-speech functionality.
- `requests`: To fetch data from external APIs (like NewsAPI).
- `json`: For handling JSON responses.
- `openai`: To interact with OpenAI's GPT models.

## Setup
1. Replace `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your **NewsAPI** key.
2. Replace `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your **OpenAI API** key.
3. Create a `musicLibrary.py` file with a dictionary containing song names and links:
   ```python
   music = {
       "song_name": "https://music_link_here.com"
   }
   ```

## Usage
1. Run the script:
   ```bash
   python personal_assistant.py
   ```
2. Say "Yuvi" to wake up the assistant.
3. Give a command, e.g., "Open Google" or "Play [song name]".

## Error Handling
- If the bot doesn't recognize your voice, try speaking more clearly.
- Ensure your microphone is working properly.
- If API requests fail, check your internet connection and API keys.

## Future Enhancements
- Add support for more voice commands.
- Integrate calendar and task management.
- Improve response accuracy with advanced AI models.

## License
This project is open-source and free to use. Feel free to modify and enhance it!


