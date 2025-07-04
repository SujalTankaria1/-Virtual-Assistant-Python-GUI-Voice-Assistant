#!/usr/bin/env python3
"""
Virtual Assistant Launcher
Choose between regular or compact GUI
"""

import sys
import os

# Add the vir directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'vir'))

def main():
    """Main launcher with GUI size options"""
    print("🤖 Virtual Assistant Launcher")
    print("=" * 40)
    print("Choose GUI size:")
    print("1. Medium GUI (550x600) - Default")
    print("2. Compact GUI (450x500) - For small screens")
    print("3. Auto-detect screen size")
    
    try:
        choice = input("\nEnter choice (1-3) or press Enter for default: ").strip()
        
        if choice == "2":
            print("Starting Compact GUI...")
            from vir.compact_gui import main as compact_main
            compact_main()
        elif choice == "3":
            # Auto-detect screen size
            import tkinter as tk
            root = tk.Tk()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            root.destroy()
            
            print(f"Detected screen size: {screen_width}x{screen_height}")
            
            if screen_width < 800 or screen_height < 700:
                print("Small screen detected. Starting Compact GUI...")
                from vir.compact_gui import main as compact_main
                compact_main()
            else:
                print("Large screen detected. Starting Medium GUI...")
                from vir.GUI import main as gui_main
                gui_main()
        else:
            print("Starting Medium GUI...")
            from vir.GUI import main as gui_main
            gui_main()
            
    except KeyboardInterrupt:
        print("\nExiting...")
    except ImportError as e:
        print(f"Import Error: {e}")
        print("\nPlease install required packages:")
        print("pip install speechrecognition pyttsx3 pillow requests pyaudio")
    except Exception as e:
        print(f"Error starting application: {e}")

if __name__ == "__main__":
    main()
