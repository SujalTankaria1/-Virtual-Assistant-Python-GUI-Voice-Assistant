import subprocess
import sys

def install_packages():
    """Install required packages for the virtual assistant"""
    packages = [
        'speechrecognition',
        'pyttsx3',
        'pillow',
        'requests',
        'pyaudio'  # Required for microphone input
    ]
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")

if __name__ == "__main__":
    install_packages()
