import pyttsx3
import threading

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.setup_voice()
    
    def setup_voice(self):
        """Configure voice properties"""
        try:
            # Get available voices
            voices = self.engine.getProperty('voices')
            if voices:
                # Set to female voice if available
                for voice in voices:
                    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                        self.engine.setProperty('voice', voice.id)
                        break
            
            # Set speech rate (words per minute)
            rate = self.engine.getProperty('rate')
            self.engine.setProperty('rate', rate - 50)  # Slower speech
            
            # Set volume (0.0 to 1.0)
            self.engine.setProperty('volume', 0.9)
            
        except Exception as e:
            print(f"Error setting up voice: {e}")
    
    def speak(self, text):
        """Convert text to speech"""
        try:
            print(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
    
    def speak_async(self, text):
        """Speak text in a separate thread to avoid blocking GUI"""
        thread = threading.Thread(target=self.speak, args=(text,))
        thread.daemon = True
        thread.start()

# Create a global instance
tts_engine = TextToSpeech()

def text_to_speech(text):
    """Wrapper function for backward compatibility"""
    tts_engine.speak_async(text)
