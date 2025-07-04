from tkinter import *
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import speech_to_text
import action
import threading
import os

class VirtualAssistantGUI:
    def __init__(self):
        self.root = Tk()
        self.setup_window()
        self.create_widgets()
        self.is_listening = False
        
    def setup_window(self):
        """Configure the main window with medium size"""
        self.root.title("AI Virtual Assistant")
        # Reduced size from 700x750 to 550x600
        self.root.geometry("550x600")
        self.root.resizable(True, True)  # Allow resizing for flexibility
        self.root.config(bg="#2C3E50")
        
        # Set minimum size to prevent too small window
        self.root.minsize(500, 550)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (550 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"550x600+{x}+{y}")
    
    def create_widgets(self):
        """Create and arrange GUI widgets with compact layout"""
        
        # Title Frame - Reduced padding
        title_frame = Frame(self.root, bg="#34495E", relief="raised", bd=2)
        title_frame.pack(pady=10, padx=15, fill="x")
        
        # Title Label - Smaller font
        title_label = Label(
            title_frame, 
            text="🤖 AI Virtual Assistant", 
            font=("Arial", 18, "bold"),  # Reduced from 24 to 18
            bg="#34495E", 
            fg="#ECF0F1"
        )
        title_label.pack(pady=8)  # Reduced padding
        
        # Image Frame - Smaller image
        image_frame = Frame(self.root, bg="#2C3E50")
        image_frame.pack(pady=5)  # Reduced padding
        
        # Load and display robot image with smaller size
        try:
            image_path = "images/resized_robot_image.png"
            if os.path.exists(image_path):
                image = Image.open(image_path)
                # Reduced image size from 200x200 to 120x120
                image = image.resize((120, 120), Image.Resampling.LANCZOS)
                self.robot_image = ImageTk.PhotoImage(image)
                image_label = Label(image_frame, image=self.robot_image, bg="#2C3E50")
                image_label.pack()
            else:
                # Smaller fallback emoji
                placeholder_label = Label(
                    image_frame, 
                    text="🤖", 
                    font=("Arial", 60),  # Reduced from 100 to 60
                    bg="#2C3E50", 
                    fg="#3498DB"
                )
                placeholder_label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")
            placeholder_label = Label(
                image_frame, 
                text="🤖", 
                font=("Arial", 60), 
                bg="#2C3E50", 
                fg="#3498DB"
            )
            placeholder_label.pack()
        
        # Status Label - Smaller font
        self.status_label = Label(
            self.root, 
            text="Ready to listen...", 
            font=("Arial", 10),  # Reduced from 12 to 10
            bg="#2C3E50", 
            fg="#95A5A6"
        )
        self.status_label.pack(pady=3)
        
        # Conversation Frame - Reduced padding
        conv_frame = Frame(self.root, bg="#2C3E50")
        conv_frame.pack(pady=10, padx=15, fill="both", expand=True)
        
        # Conversation Text Area - Reduced height
        self.text_area = scrolledtext.ScrolledText(
            conv_frame,
            font=("Arial", 9),  # Reduced font size
            bg="#ECF0F1",
            fg="#2C3E50",
            height=8,  # Reduced from 12 to 8
            wrap=WORD,
            state=DISABLED
        )
        self.text_area.pack(fill="both", expand=True)
        
        # Input Frame - Reduced padding
        input_frame = Frame(self.root, bg="#2C3E50")
        input_frame.pack(pady=8, padx=15, fill="x")
        
        # Text Input - Smaller font
        self.entry = Entry(
            input_frame,
            font=("Arial", 10),  # Reduced from 12 to 10
            bg="#ECF0F1",
            fg="#2C3E50",
            relief="solid",
            bd=1
        )
        self.entry.pack(side=LEFT, fill="x", expand=True, padx=(0, 8))
        self.entry.bind("<Return>", lambda event: self.send_text())
        
        # Send Button - Smaller
        self.send_button = Button(
            input_frame,
            text="SEND",
            font=("Arial", 9, "bold"),  # Reduced font
            bg="#27AE60",
            fg="white",
            relief="flat",
            padx=15,  # Reduced padding
            command=self.send_text
        )
        self.send_button.pack(side=RIGHT)
        
        # Button Frame - Reduced padding
        button_frame = Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=15)
        
        # Buttons with smaller size and reduced padding
        button_config = {
            "font": ("Arial", 11, "bold"),  # Reduced from 14 to 11
            "relief": "flat",
            "padx": 20,  # Reduced from 30 to 20
            "pady": 8    # Reduced from 10 to 8
        }
        
        # Ask Button (Voice Input)
        self.ask_button = Button(
            button_frame,
            text="🎤 ASK",
            bg="#3498DB",
            fg="white",
            command=self.ask_voice,
            **button_config
        )
        self.ask_button.pack(side=LEFT, padx=8)  # Reduced padding between buttons
        
        # Clear Button
        self.clear_button = Button(
            button_frame,
            text="🗑️ CLEAR",
            bg="#E74C3C",
            fg="white",
            command=self.clear_conversation,
            **button_config
        )
        self.clear_button.pack(side=LEFT, padx=8)
        
        # Exit Button
        self.exit_button = Button(
            button_frame,
            text="❌ EXIT",
            bg="#95A5A6",
            fg="white",
            command=self.exit_app,
            **button_config
        )
        self.exit_button.pack(side=LEFT, padx=8)
    
    def update_conversation(self, speaker, message):
        """Update the conversation display"""
        self.text_area.config(state=NORMAL)
        self.text_area.insert(END, f"{speaker}: {message}\n\n")
        self.text_area.config(state=DISABLED)
        self.text_area.see(END)
    
    def update_status(self, status):
        """Update the status label"""
        self.status_label.config(text=status)
        self.root.update()
    
    def ask_voice(self):
        """Handle voice input in a separate thread"""
        if self.is_listening:
            return
        
        def voice_thread():
            self.is_listening = True
            self.ask_button.config(state=DISABLED, text="🎤 LISTENING...")
            self.update_status("Listening... Please speak now")
            
            try:
                # Get voice input
                user_input = speech_to_text.speech_to_text()
                
                if user_input and user_input not in ["timeout", "unknown", "error"]:
                    self.update_conversation("You", user_input)
                    self.update_status("Processing your request...")
                    
                    # Process the input
                    response = action.action(user_input)
                    
                    if response:
                        self.update_conversation("Assistant", response)
                        
                        # Check if shutdown was requested
                        if response == "shutdown":
                            self.root.after(2000, self.exit_app)  # Exit after 2 seconds
                else:
                    if user_input == "timeout":
                        self.update_conversation("System", "No speech detected. Please try again.")
                    elif user_input == "unknown":
                        self.update_conversation("System", "Could not understand speech. Please try again.")
                    else:
                        self.update_conversation("System", "Error processing speech. Please try again.")
                
            except Exception as e:
                self.update_conversation("System", f"An error occurred: {str(e)}")
            
            finally:
                self.is_listening = False
                self.ask_button.config(state=NORMAL, text="🎤 ASK")
                self.update_status("Ready to listen...")
        
        # Start voice processing in a separate thread
        thread = threading.Thread(target=voice_thread)
        thread.daemon = True
        thread.start()
    
    def send_text(self):
        """Handle text input"""
        user_input = self.entry.get().strip()
        if user_input:
            self.entry.delete(0, END)
            self.update_conversation("You", user_input)
            self.update_status("Processing your request...")
            
            # Process the input
            response = action.action(user_input)
            
            if response:
                self.update_conversation("Assistant", response)
                
                # Check if shutdown was requested
                if response == "shutdown":
                    self.root.after(2000, self.exit_app)  # Exit after 2 seconds
            
            self.update_status("Ready to listen...")
    
    def clear_conversation(self):
        """Clear the conversation history"""
        self.text_area.config(state=NORMAL)
        self.text_area.delete(1.0, END)
        self.text_area.config(state=DISABLED)
        self.update_status("Conversation cleared. Ready to listen...")
    
    def exit_app(self):
        """Exit the application"""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()
    
    def run(self):
        """Start the GUI application"""
        # Welcome message
        self.update_conversation("Assistant", "Hello! I'm your virtual assistant. Click 'ASK' to speak or type your message below.")
        self.root.mainloop()

def main():
    """Main function to run the application"""
    try:
        app = VirtualAssistantGUI()
        app.run()
    except Exception as e:
        print(f"Error starting application: {e}")
        messagebox.showerror("Error", f"Failed to start the application: {e}")

if __name__ == "__main__":
    main()
