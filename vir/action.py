import text_to_speech
import datetime
import webbrowser
import weather
import os
import subprocess
import platform

def action(user_input):
    """
    Process user input and perform corresponding actions
    """
    if not user_input or user_input in ["timeout", "unknown", "error"]:
        if user_input == "timeout":
            return "I didn't hear anything. Please try again."
        elif user_input == "unknown":
            return "I couldn't understand what you said. Please speak clearly."
        else:
            return "There was an error processing your request."
    
    user_data = user_input.lower().strip()
    
    # Greeting responses
    if any(word in user_data for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
        response = "Hello! How can I help you today?"
        text_to_speech.text_to_speech(response)
        return response
    
    # Name inquiry
    elif any(phrase in user_data for phrase in ["what is your name", "your name", "who are you"]):
        response = "My name is Virtual Assistant. I'm here to help you!"
        text_to_speech.text_to_speech(response)
        return response
    
    # Time inquiry
    elif any(phrase in user_data for phrase in ["time", "what time", "current time"]):
        current_time = datetime.datetime.now()
        time_str = current_time.strftime("%I:%M %p")
        response = f"The current time is {time_str}"
        text_to_speech.text_to_speech(response)
        return response
    
    # Date inquiry
    elif any(phrase in user_data for phrase in ["date", "what date", "today's date"]):
        current_date = datetime.datetime.now()
        date_str = current_date.strftime("%B %d, %Y")
        response = f"Today's date is {date_str}"
        text_to_speech.text_to_speech(response)
        return response
    
    # Weather inquiry
    elif any(word in user_data for word in ["weather", "temperature", "climate"]):
        response = weather.weather()
        text_to_speech.text_to_speech(response)
        return response
    
    # Open Google
    elif any(phrase in user_data for phrase in ["open google", "google", "search google"]):
        webbrowser.open("https://www.google.com")
        response = "Opening Google for you!"
        text_to_speech.text_to_speech(response)
        return response
    
    # Open YouTube
    elif any(phrase in user_data for phrase in ["open youtube", "youtube", "open video"]):
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube for you!"
        text_to_speech.text_to_speech(response)
        return response
    
    # Open Calculator
    elif any(word in user_data for word in ["calculator", "calculate", "calc"]):
        try:
            if platform.system() == "Windows":
                subprocess.run("calc.exe")
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", "-a", "Calculator"])
            else:  # Linux
                subprocess.run(["gnome-calculator"])
            response = "Opening calculator for you!"
            text_to_speech.text_to_speech(response)
            return response
        except:
            response = "Sorry, I couldn't open the calculator."
            text_to_speech.text_to_speech(response)
            return response
    
    # Open Notepad
    elif any(word in user_data for word in ["notepad", "text editor", "note"]):
        try:
            if platform.system() == "Windows":
                subprocess.run("notepad.exe")
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", "-a", "TextEdit"])
            else:  # Linux
                subprocess.run(["gedit"])
            response = "Opening text editor for you!"
            text_to_speech.text_to_speech(response)
            return response
        except:
            response = "Sorry, I couldn't open the text editor."
            text_to_speech.text_to_speech(response)
            return response
    
    # Shutdown/Exit
    elif any(word in user_data for word in ["shutdown", "exit", "quit", "bye", "goodbye"]):
        response = "Goodbye! Have a great day!"
        text_to_speech.text_to_speech(response)
        return "shutdown"
    
    # Help
    elif any(word in user_data for word in ["help", "what can you do", "commands"]):
        response = """I can help you with:
        - Tell you the current time and date
        - Get weather information
        - Open Google, YouTube, Calculator, or Notepad
        - Answer basic questions
        Just speak naturally and I'll try to help!"""
        text_to_speech.text_to_speech("I can help you with time, weather, opening applications, and answering basic questions. Just speak naturally!")
        return response
    
    # Default response
    else:
        response = "I'm sorry, I didn't understand that. You can ask me about time, weather, or ask me to open applications like Google or YouTube."
        text_to_speech.text_to_speech(response)
        return response
