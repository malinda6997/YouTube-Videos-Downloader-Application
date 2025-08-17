#!/usr/bin/env python3
"""
Cross-platform launcher for YouTube Video Downloader
"""

import sys
import os

def main():
    """Launch the YouTube Video Downloader application"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add the project root to Python path
    sys.path.insert(0, script_dir)
    
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
