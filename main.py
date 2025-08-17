"""
Main entry point for YouTube Video Downloader Application
MVC Architecture Implementation with Splash Screen
"""

import sys
import os
from splash import show_splash_screen
from controller import YouTubeDownloaderController


def main():
    """Main function to start the YouTube Video Downloader application"""
    try:
        # Show splash screen first
        show_splash_screen()
        
        # Create and run the main application
        app = YouTubeDownloaderController()
        app.run()
        
    except ImportError as e:
        print(f"Import Error: {e}")
        print("Please make sure all required packages are installed:")
        print("- yt-dlp")
        print("- tkinter (usually comes with Python)")
        print("\nYou can install missing packages using:")
        print("pip install yt-dlp")
        sys.exit(1)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Add current directory to Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    main()
