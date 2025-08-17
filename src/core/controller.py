"""
Controller module for YouTube Video Downloader
Manages interaction between Model and View components
"""

import sys
import os

# Add src directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from core.model import YouTubeDownloaderModel
from ui.view import YouTubeDownloaderView
import threading


class YouTubeDownloaderController:
    """Controller class that manages interaction between Model and View"""
    
    def __init__(self):
        self.model = YouTubeDownloaderModel()
        self.view = YouTubeDownloaderView()
        
        # Set up callbacks
        self.setup_callbacks()
    
    def setup_callbacks(self):
        """Setup callback functions for the view"""
        self.view.set_callbacks(
            download_callback=self.handle_download,
            validate_url_callback=self.model.validate_url,
            get_info_callback=self.handle_get_info
        )
    
    def handle_download(self, url: str):
        """Handle video download request"""
        try:
            # Update UI to show download starting
            self.view.root.after(0, self.view.show_progress)
            self.view.root.after(0, self.view.disable_buttons)
            self.view.root.after(0, self.view.show_info_message, "Starting download...")
            
            # Progress callback function
            def progress_callback(percent: str, speed: str):
                self.view.root.after(0, self.view.update_progress, percent, speed)
            
            # Perform download
            result = self.model.download_video(url, progress_callback)
            
            # Update UI based on result
            if result['success']:
                self.view.root.after(0, self.view.show_success, result['message'])
            else:
                # Check if it's a playlist error and provide helpful guidance
                if result.get('is_playlist') and result.get('first_video_url'):
                    error_msg = f"{result['error']}\n\nDid you want to download the first video instead?\nFirst video URL: {result['first_video_url']}"
                    self.view.root.after(0, self.view.show_playlist_error, error_msg, result['first_video_url'])
                else:
                    self.view.root.after(0, self.view.show_error, result['error'])
            
        except Exception as e:
            self.view.root.after(0, self.view.show_error, f"Unexpected error: {str(e)}")
        
        finally:
            # Re-enable buttons
            self.view.root.after(0, self.view.enable_buttons)
    
    def handle_get_info(self, url: str):
        """Handle get video info request"""
        try:
            # Update UI to show info retrieval starting
            self.view.root.after(0, self.view.show_progress)
            self.view.root.after(0, self.view.disable_buttons)
            self.view.root.after(0, self.view.show_info_message, "Retrieving video information...")
            
            # Get video information
            info = self.model.get_video_info(url)
            
            if info:
                # Add additional information for the display
                info['url'] = url
                info['download_path'] = self.model.download_path
                
                # Show information in separate window
                self.view.root.after(0, self.view.show_video_info_window, info)
                self.view.root.after(0, self.view.show_success, "Video information retrieved successfully")
            else:
                self.view.root.after(0, self.view.show_error, "Failed to retrieve video information")
            
        except Exception as e:
            self.view.root.after(0, self.view.show_error, f"Error retrieving info: {str(e)}")
        
        finally:
            # Re-enable buttons and hide progress
            self.view.root.after(0, self.view.enable_buttons)
            self.view.root.after(0, self.view.hide_progress)
    
    def format_video_info(self, info: dict) -> str:
        """Format video information for display"""
        duration_minutes = info['duration'] // 60 if info['duration'] else 0
        duration_seconds = info['duration'] % 60 if info['duration'] else 0
        
        # Format view count
        view_count = info.get('view_count', 0)
        if view_count >= 1000000:
            view_count_str = f"{view_count // 1000000:.1f}M views"
        elif view_count >= 1000:
            view_count_str = f"{view_count // 1000:.1f}K views"
        else:
            view_count_str = f"{view_count} views"
        
        # Format upload date
        upload_date = info.get('upload_date', 'Unknown')
        if upload_date != 'Unknown' and len(upload_date) == 8:
            # Convert YYYYMMDD to YYYY-MM-DD
            formatted_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
        else:
            formatted_date = upload_date
        
        info_text = f"""Video Information:

Title: {info.get('title', 'Unknown Title')}

Uploader: {info.get('uploader', 'Unknown Uploader')}

Duration: {duration_minutes:02d}:{duration_seconds:02d}

Views: {view_count_str}

Upload Date: {formatted_date}

Download Path: {self.model.download_path}
"""
        
        return info_text
    
    def run(self):
        """Start the application"""
        self.view.run()
    
    def set_download_path(self, path: str):
        """Set custom download path"""
        self.model.set_download_path(path)
    
    def get_download_path(self) -> str:
        """Get current download path"""
        return self.model.download_path
