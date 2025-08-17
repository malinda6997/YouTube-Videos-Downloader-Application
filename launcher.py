#!/usr/bin/env python3
"""
YouTube Video Downloader - Application Launcher
Developed by Malinda Prabath
"""

import sys
import os

def main():
    """Launch the YouTube Video Downloader application"""
    # Get the directory where this launcher script is located
    root_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(root_dir, 'src')
    
    # Add src directory to Python path
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    
    # Import and run the main application
    try:
        from main import main as app_main
        app_main()
    except ImportError as e:
        print(f"Error: Could not import application: {e}")
        print("Please make sure all dependencies are installed.")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
