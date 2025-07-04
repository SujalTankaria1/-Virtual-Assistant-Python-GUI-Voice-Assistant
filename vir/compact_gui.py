"""
Alternative Compact GUI Version
Even smaller interface for very small screens
"""

from tkinter import *
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import speech_to_text
import action
import threading
import os

class CompactVirtualAssistantGUI:
    def __init__(self):
        self.root = Tk()
        self.setup_window()
        self.create_widgets()
        self.is_listening = False
        
    def setup_window(self):
        """Configure the main window with compact size"""
        self.root.title("AI Assistant")
        # Very compact size for small screens
        self.root.geometry("450x500")
        self.root.resizable(True, True)
        self.root.config(bg="#2C3E50")
        
        # Set minimum size
        self.root.minsize(400, 450)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"450x500+{x}+{y}")
    
    def create_widgets(self):
        """Create compact widget layout"""
        
        # Compact Title
        title_label = Label(
            self.root, 
            text="🤖 AI Assistant", 
            font=("Arial", 14, "bold"),
            bg="#2C3E50", 
            fg="#ECF0F1"
        )
        title_label.pack(pady=5)
        
        # Small robot icon
        icon_label = Label(
            self.root, 
            text="🤖", 
            font=("Arial", 40),
            bg="#2C3E50", 
            fg="#3498DB"
        )
        icon_label.pack(pady=5)
        
        # Status
        self.status_label = Label(
            self.root, 
            text="Ready", 
            font=("Arial", 9),
            bg="#2C3E50", 
            fg="#95A5A6"
        )
        self.status_label.pack()
        
        # Conversation area
        self.text_area = scrolledtext.ScrolledText(
            self.root,
            font=("Arial", 8),
            bg="#ECF0F1",
            fg="#2C3E50",
            height=12,
            wrap=WORD,
            state=DISABLED
        )
        self.text_area.pack(pady=5, padx=10, fill="both", expand=True)
        
        # Input frame
        input_frame = Frame(self.root, bg="#2C3E50")
        input_frame.pack(pady=5, padx=10, fill="x")
        
        self.entry = Entry(
            input_frame,
            font=("Arial", 9),
            bg="#ECF0F1",
            fg="#2C3E50"
        )
        self.entry.pack(side=LEFT, fill="x", expand=True, padx=(0, 5))
        self.entry.bind("<Return>", lambda event: self.send_text())
        
        Button(
            input_frame,
            text="Send",
            font=("Arial", 8),
            bg="#27AE60",
            fg="white",
            command=self.send_text
        ).pack(side=RIGHT)
        
        # Compact button frame
        button_frame = Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=10)
        
        # Compact buttons
        self.ask_button = Button(
            button_frame,
            text="🎤 ASK",
            font=("Arial", 9, "bold"),
            bg="#3498DB",
            fg="white",
            padx=15,
            pady=5,
            command=self.ask_voice
        )
        self.ask_button.pack(side=LEFT, padx=5)
        
        Button(
            button_frame,
            text="Clear",
            font=("Arial", 9),
            bg="#E74C3C",
            fg="white",
            padx=15,
            pady=5,
            command=self.clear_conversation
        ).pack(side=LEFT, padx=5)
        
        Button(
            button_frame,
            text="Exit",
            font=("Arial", 9),
            bg="#95A5A6",
            fg="white",
            padx=15,
            pady=5,
            command=self.exit_app
        ).pack(side=LEFT, padx=5)
    
    def update_conversation(self, speaker, message):
        """Update the conversation display"""
        self.text_area.config(state=NORMAL)
        self.text_area.insert(END, f"{speaker}: {message}\n")
        self.text_area.config(state=DISABLED)
        self.text_area.see(END)
    
    def update_status(self, status):
        """Update the status label"""
        self.status_label.config(text=status)
        self.root.update()
    
    def ask_voice(self):
        """Handle voice input"""
        if self.is_listening:
            return
        
        def voice_thread():
            self.is_listening = True
            self.ask_button.config(state=DISABLED, text="Listening...")
            self.update_status("Listening...")
            
            try:
                user_input = speech_to_text.speech_to_text()
                
                if user_input and user_input not in ["timeout", "unknown", "error"]:
                    self.update_conversation("You", user_input)
                    self.update_status("Processing...")
                    
                    response = action.action(user_input)
                    
                    if response:
                        self.update_conversation("Bot", response)
                        
                        if response == "shutdown":
                            self.root.after(2000, self.exit_app)
                else:
                    self.update_conversation("System", "Could not understand. Try again.")
                
            except Exception as e:
                self.update_conversation("System", f"Error: {str(e)}")
            
            finally:
                self.is_listening = False
                self.ask_button.config(state=NORMAL, text="🎤 ASK")
                self.update_status("Ready")
        
        thread = threading.Thread(target=voice_thread)
        thread.daemon = True
        thread.start()
    
    def send_text(self):
        """Handle text input"""
        user_input = self.entry.get().strip()
        if user_input:
            self.entry.delete(0, END)
            self.update_conversation("You", user_input)
            self.update_status("Processing...")
            
            response = action.action(user_input)
            
            if response:
                self.update_conversation("Bot", response)
                
                if response == "shutdown":
                    self.root.after(2000, self.exit_app)
            
            self.update_status("Ready")
    
    def clear_conversation(self):
        """Clear the conversation history"""
        self.text_area.config(state=NORMAL)
        self.text_area.delete(1.0, END)
        self.text_area.config(state=DISABLED)
        self.update_status("Cleared")
    
    def exit_app(self):
        """Exit the application"""
        self.root.destroy()
    
    def run(self):
        """Start the GUI application"""
        self.update_conversation("Bot", "Hello! Click ASK to speak or type below.")
        self.root.mainloop()

def main():
    """Main function for compact GUI"""
    try:
        app = CompactVirtualAssistantGUI()
        app.run()
    except Exception as e:
        print(f"Error starting application: {e}")

if __name__ == "__main__":
    main()
