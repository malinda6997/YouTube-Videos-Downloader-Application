"""
Configuration settings for YouTube Video Downloader
"""

import os

class Config:
    """Configuration class for the application"""
    
    # Default download settings
    DEFAULT_DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "YouTube_Videos")
    DEFAULT_QUALITY = "best[height<=720]"  # Download best quality up to 720p
    
    # GUI settings
    WINDOW_TITLE = "YouTube Video Downloader"
    WINDOW_SIZE = "600x500"
    BACKGROUND_COLOR = "white"
    
    # Colors
    PRIMARY_COLOR = "#4CAF50"      # Green
    SECONDARY_COLOR = "#2196F3"    # Blue
    DANGER_COLOR = "#F44336"       # Red
    WARNING_COLOR = "#FF5722"      # Deep Orange
    TEXT_COLOR = "#333333"         # Dark Gray
    SUBTITLE_COLOR = "#666666"     # Medium Gray
    
    # Fonts
    TITLE_FONT = ("Arial", 24, "bold")
    SUBTITLE_FONT = ("Arial", 14)
    BUTTON_FONT = ("Arial", 12, "bold")
    TEXT_FONT = ("Arial", 12)
    SMALL_FONT = ("Arial", 10)
    
    # Download settings
    MAX_RETRIES = 3
    TIMEOUT = 30  # seconds
    
    # Supported domains
    YOUTUBE_DOMAINS = [
        'youtube.com',
        'youtu.be',
        'www.youtube.com',
        'm.youtube.com'
    ]
