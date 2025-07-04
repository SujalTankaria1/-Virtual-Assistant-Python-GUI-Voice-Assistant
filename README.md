# Virtual Assistant

A Python-based virtual assistant with GUI interface using tkinter, speech recognition, and text-to-speech capabilities.

## Features

- 🎤 Voice recognition and speech-to-text conversion
- 🔊 Text-to-speech responses
- 🌤️ Weather information
- ⏰ Time and date queries
- �� Web browser integration (Google, YouTube)
- 🧮 System application launching (Calculator, Notepad)
- 💬 Interactive GUI with conversation history
- ⌨️ Both voice and text input support

## Installation

1. **Install Python 3.7 or higher**

2. **Install required packages:**
   \`\`\`bash
   pip install speechrecognition pyttsx3 pillow requests pyaudio
   \`\`\`

3. **For Windows users (if pyaudio installation fails):**
   \`\`\`bash
   pip install pipwin
   pipwin install pyaudio
   \`\`\`

4. **For Linux users:**
   \`\`\`bash
   sudo apt-get install python3-pyaudio
   \`\`\`

5. **For macOS users:**
   \`\`\`bash
   brew install portaudio
   pip install pyaudio
   \`\`\`

## Usage

1. **Run the application:**
   \`\`\`bash
   python run_assistant.py
   \`\`\`

2. **Using the GUI:**
   - Click the "🎤 ASK" button to use voice input
   - Type in the text box and press Enter or click "SEND" for text input
   - Use "🗑️ CLEAR" to clear conversation history
   - Use "❌ EXIT" to close the application

## Voice Commands

The assistant can respond to various commands:

- **Greetings:** "Hello", "Hi", "Good morning"
- **Identity:** "What is your name?", "Who are you?"
- **Time:** "What time is it?", "Current time"
- **Date:** "What's the date?", "Today's date"
- **Weather:** "Weather", "Temperature"
- **Web browsing:** "Open Google", "Open YouTube"
- **Applications:** "Open calculator", "Open notepad"
- **Help:** "Help", "What can you do?"
- **Exit:** "Goodbye", "Exit", "Shutdown"

## File Structure

\`\`\`
Virtual Assistant/
├── vir/
│   ├── GUI.py              # Main GUI interface
│   ├── action.py           # Command processing logic
│   ├── speech_to_text.py   # Speech recognition
│   ├── text_to_speech.py   # Text-to-speech conversion
│   └── weather.py          # Weather information
├── images/
│   └── resized_robot_image.png  # Robot avatar
|   └── SS_of_terminal.png  # Screenshot of the Terminal 
|   └── Virtual_Assistant_eg.png  # Example of Virtual Assistant
├── scripts/
│   └── install_requirements.py  # Package installer
├── run_assistant.py        # Main launcher
└── README.md              # This file
\`\`\`

## Troubleshooting

1. **Microphone not working:**
   - Check microphone permissions
   - Ensure microphone is not being used by other applications
   - Try running as administrator (Windows)

2. **Speech recognition errors:**
   - Speak clearly and at moderate pace
   - Ensure stable internet connection (Google Speech API requires internet)
   - Check microphone volume levels

3. **Text-to-speech not working:**
   - Check system audio settings
   - Ensure speakers/headphones are connected
   - Try different voice settings in the code

4. **Import errors:**
   - Ensure all required packages are installed
   - Check Python version compatibility
   - Try reinstalling packages

## Customization

You can customize the assistant by:

- Adding new commands in `action.py`
- Modifying the GUI appearance in `GUI.py`
- Changing voice settings in `text_to_speech.py`
- Adding new weather locations in `weather.py`

## Requirements

- Python 3.7+
- speechrecognition
- pyttsx3
- pillow
- requests
- pyaudio
- tkinter (usually included with Python)

## License

This project is open source and available under the MIT License.
