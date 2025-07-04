import speech_recognition as sr
import threading
import time

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
    
    def speech_to_text(self, timeout=5, phrase_time_limit=5):
        """
        Convert speech to text with improved error handling
        """
        try:
            print("Listening...")
            with self.microphone as source:
                # Listen for audio with timeout
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            print("Processing...")
            # Recognize speech using Google Speech Recognition
            voice_data = self.recognizer.recognize_google(audio)
            print(f"You said: {voice_data}")
            return voice_data.lower()
            
        except sr.WaitTimeoutError:
            print("Listening timeout - no speech detected")
            return "timeout"
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "unknown"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "error"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "error"

# Create a global instance
speech_recognizer = SpeechToText()

def speech_to_text():
    """Wrapper function for backward compatibility"""
    return speech_recognizer.speech_to_text()
