"""
Test the new video info window functionality
"""

import sys
import os

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import tkinter as tk
from view import VideoInfoWindow

def test_info_window():
    """Test the video info window with sample data"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Sample video information
    sample_info = {
        'title': 'Sample YouTube Video Title - How to Learn Python Programming',
        'uploader': 'TechChannel123',
        'duration': 3665,  # 1 hour, 1 minute, 5 seconds
        'view_count': 1234567,
        'upload_date': '20240315',
        'filesize': 157286400,  # ~150 MB
        'url': 'https://www.youtube.com/watch?v=sample123',
        'download_path': r'C:\Users\YourName\Downloads\YouTube_Videos'
    }
    
    # Create and show the info window
    info_window = VideoInfoWindow(root, sample_info)
    
    root.mainloop()

if __name__ == "__main__":
    test_info_window()
