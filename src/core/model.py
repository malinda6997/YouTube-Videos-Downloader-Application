"""
Model module for YouTube Video Downloader
Handles the core download functionality using yt-dlp
"""

import yt_dlp
import os
from typing import Optional, Callable


class YouTubeDownloaderModel:
    """Model class that handles YouTube video downloading logic"""
    
    def __init__(self):
        self.download_path = os.path.join(os.path.expanduser("~"), "Downloads", "YouTube_Videos")
        self._create_download_directory()
    
    def _create_download_directory(self):
        """Create download directory if it doesn't exist"""
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
    
    def set_download_path(self, path: str):
        """Set custom download path"""
        self.download_path = path
        self._create_download_directory()
    
    def validate_url(self, url: str) -> bool:
        """Validate if the provided URL is a valid YouTube URL"""
        if not url or not isinstance(url, str):
            return False
        
        youtube_domains = ['youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com']
        return any(domain in url.lower() for domain in youtube_domains)
    
    def get_video_info(self, url: str) -> Optional[dict]:
        """Get video information without downloading"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': True,  # For playlist detection
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Check if this is a playlist
                if info.get('_type') == 'playlist':
                    return {
                        'title': info.get('title', 'Unknown Playlist'),
                        'duration': 0,
                        'uploader': 'Playlist',
                        'view_count': 0,
                        'upload_date': 'N/A',
                        'filesize': 0,
                        'description': f"This is a playlist with {len(info.get('entries', []))} videos. Please use the direct video URL instead of the playlist URL.",
                        'is_playlist': True,
                        'playlist_count': len(info.get('entries', [])),
                        'first_video_url': f"https://www.youtube.com/watch?v={info['entries'][0]['id']}" if info.get('entries') else None
                    }
                
                # If it's a single video, get detailed info
                ydl_opts['extract_flat'] = False
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_detailed:
                    info = ydl_detailed.extract_info(url, download=False)
                
                # Get the best format for size estimation
                formats = info.get('formats', [])
                best_format = None
                for fmt in formats:
                    if fmt.get('vcodec') != 'none' and fmt.get('height', 0) <= 720:
                        if not best_format or (fmt.get('height', 0) > best_format.get('height', 0)):
                            best_format = fmt
                
                filesize = best_format.get('filesize', 0) if best_format else 0
                
                return {
                    'title': info.get('title', 'Unknown Title'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown Uploader'),
                    'view_count': info.get('view_count', 0),
                    'upload_date': info.get('upload_date', 'Unknown Date'),
                    'filesize': filesize,
                    'description': info.get('description', 'No description available')[:200] + '...' if info.get('description') else 'No description available'
                }
        except Exception as e:
            print(f"Error getting video info: {str(e)}")
            return None
    
    def download_video(self, url: str, progress_callback: Optional[Callable] = None) -> dict:
        """
        Download video from YouTube URL
        Returns status dictionary with success/error information
        """
        if not self.validate_url(url):
            return {
                'success': False,
                'error': 'Invalid YouTube URL provided'
            }
        
        # Check if it's a playlist first
        try:
            ydl_opts_check = {
                'quiet': True,
                'extract_flat': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts_check) as ydl:
                info = ydl.extract_info(url, download=False)
                if info.get('_type') == 'playlist':
                    return {
                        'success': False,
                        'error': f'Playlist detected with {len(info.get("entries", []))} videos. Please use a direct video URL instead of playlist URL.',
                        'is_playlist': True,
                        'first_video_url': f"https://www.youtube.com/watch?v={info['entries'][0]['id']}" if info.get('entries') else None
                    }
        except:
            pass  # Continue with normal download if playlist check fails
        
        try:
            def progress_hook(d):
                if progress_callback and d['status'] == 'downloading':
                    percent = d.get('_percent_str', '0%')
                    speed = d.get('_speed_str', 'N/A')
                    progress_callback(percent, speed)
            
            ydl_opts = {
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'format': 'best[height<=720]',  # Download best quality up to 720p
                'progress_hooks': [progress_hook],
                'noplaylist': True,  # Download only the video, not the playlist
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            return {
                'success': True,
                'message': f'Video downloaded successfully to {self.download_path}'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Download failed: {str(e)}'
            }
    
    def get_available_formats(self, url: str) -> Optional[list]:
        """Get available formats for the video"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                formats = info.get('formats', [])
                
                # Filter and format the available formats
                available_formats = []
                for fmt in formats:
                    if fmt.get('vcodec') != 'none':  # Video formats only
                        available_formats.append({
                            'format_id': fmt.get('format_id'),
                            'ext': fmt.get('ext'),
                            'resolution': fmt.get('resolution', 'Unknown'),
                            'filesize': fmt.get('filesize', 0)
                        })
                
                return available_formats
        except Exception as e:
            print(f"Error getting formats: {str(e)}")
            return None
