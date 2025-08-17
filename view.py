"""
View module for YouTube Video Downloader
Handles the GUI interface using tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
from typing import Callable, Optional


class VideoInfoWindow:
    """Separate window for displaying video information"""
    
    def __init__(self, parent, video_info: dict):
        self.parent = parent
        self.video_info = video_info
        self.window = tk.Toplevel(parent)
        self.window.title("Video Information")
        self.window.geometry("500x600")
        self.window.configure(bg="white")
        self.window.resizable(True, True)
        
        # Make window modal
        self.window.transient(parent)
        self.window.grab_set()
        
        # Center the window
        self.center_window()
        
        self.setup_ui()
    
    def center_window(self):
        """Center the window on the screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
    
    def setup_ui(self):
        """Setup the video information UI"""
        # Main container
        main_frame = tk.Frame(self.window, bg="white", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Video Information",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#333333"
        )
        title_label.pack(pady=(0, 20))
        
        # Information display area
        info_frame = tk.Frame(main_frame, bg="white")
        info_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Scrollable text area for video info
        self.info_text = scrolledtext.ScrolledText(
            info_frame,
            font=("Arial", 11),
            bg="#F8F9FA",
            fg="#333333",
            relief=tk.SOLID,
            bd=1,
            padx=15,
            pady=15,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.info_text.pack(fill=tk.BOTH, expand=True)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="white")
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Copy button
        self.copy_btn = tk.Button(
            buttons_frame,
            text="📋 Copy Information",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.copy_info
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Close button
        self.close_btn = tk.Button(
            buttons_frame,
            text="Close",
            font=("Arial", 12),
            bg="#666666",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.close_window
        )
        self.close_btn.pack(side=tk.RIGHT)
        
        # Display the video information
        self.display_info()
    
    def display_info(self):
        """Display formatted video information"""
        info_text = self.format_video_info()
        
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, info_text)
        self.info_text.config(state=tk.DISABLED)
    
    def format_video_info(self) -> str:
        """Format video information for display"""
        info = self.video_info
        
        # Format duration
        duration = info.get('duration', 0)
        if duration:
            hours = duration // 3600
            minutes = (duration % 3600) // 60
            seconds = duration % 60
            if hours > 0:
                duration_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            else:
                duration_str = f"{minutes:02d}:{seconds:02d}"
        else:
            duration_str = "Unknown"
        
        # Format view count
        view_count = info.get('view_count', 0)
        if view_count >= 1000000:
            view_count_str = f"{view_count:,} ({view_count // 1000000:.1f}M views)"
        elif view_count >= 1000:
            view_count_str = f"{view_count:,} ({view_count // 1000:.1f}K views)"
        else:
            view_count_str = f"{view_count:,} views" if view_count else "Unknown"
        
        # Format upload date
        upload_date = info.get('upload_date', 'Unknown')
        if upload_date != 'Unknown' and len(upload_date) == 8:
            formatted_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
        else:
            formatted_date = upload_date
        
        # Format file size if available
        filesize = info.get('filesize', 0)
        if filesize:
            if filesize >= 1024*1024*1024:  # GB
                filesize_str = f"{filesize/(1024*1024*1024):.2f} GB"
            elif filesize >= 1024*1024:  # MB
                filesize_str = f"{filesize/(1024*1024):.2f} MB"
            else:  # KB
                filesize_str = f"{filesize/1024:.2f} KB"
        else:
            filesize_str = "Unknown"
        
        info_text = f"""╔════════════════════════════════════════════════════════════════╗
║                           VIDEO DETAILS                           ║
╚════════════════════════════════════════════════════════════════╝

📺 TITLE:
{info.get('title', 'Unknown Title')}

👤 UPLOADER:
{info.get('uploader', 'Unknown Uploader')}

⏱️ DURATION:
{duration_str}

👁️ VIEWS:
{view_count_str}

📅 UPLOAD DATE:
{formatted_date}

📏 ESTIMATED SIZE:
{filesize_str}

🎥 QUALITY:
Best available up to 720p

📂 DOWNLOAD PATH:
{info.get('download_path', 'Default Downloads Folder')}

📋 VIDEO URL:
{info.get('url', 'N/A')}

════════════════════════════════════════════════════════════════

💡 TIP: Click "Copy Information" to copy all details to clipboard
"""
        
        return info_text
    
    def copy_info(self):
        """Copy video information to clipboard"""
        try:
            info_text = self.format_video_info()
            self.window.clipboard_clear()
            self.window.clipboard_append(info_text)
            
            # Show success message
            messagebox.showinfo("Copied!", "Video information copied to clipboard!", parent=self.window)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}", parent=self.window)
    
    def close_window(self):
        """Close the information window"""
        self.window.grab_release()
        self.window.destroy()


class YouTubeDownloaderView:
    """View class that handles the GUI interface"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x500")
        self.root.configure(bg="white")
        self.root.resizable(True, True)
        
        # Center the window
        self.center_window()
        
        # Initialize UI components
        self.url_var = tk.StringVar()
        self.progress_var = tk.StringVar()
        self.status_var = tk.StringVar()
        
        # Callbacks (to be set by controller)
        self.download_callback: Optional[Callable] = None
        self.validate_url_callback: Optional[Callable] = None
        self.get_info_callback: Optional[Callable] = None
        
        self.setup_ui()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def setup_ui(self):
        """Setup the main UI components"""
        # Main container
        main_frame = tk.Frame(self.root, bg="white", padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="YouTube Video Downloader",
            font=("Arial", 24, "bold"),
            bg="white",
            fg="#333333"
        )
        title_label.pack(pady=(0, 30))
        
        # URL input section
        url_frame = tk.Frame(main_frame, bg="white")
        url_frame.pack(fill=tk.X, pady=(0, 20))
        
        url_label = tk.Label(
            url_frame,
            text="Please enter your link:",
            font=("Arial", 14),
            bg="white",
            fg="#666666"
        )
        url_label.pack(anchor=tk.W, pady=(0, 10))
        
        # URL entry
        self.url_entry = tk.Entry(
            url_frame,
            textvariable=self.url_var,
            font=("Arial", 12),
            width=50,
            relief=tk.SOLID,
            bd=1,
            highlightthickness=2,
            highlightcolor="#4CAF50",
            highlightbackground="#E0E0E0"
        )
        self.url_entry.pack(fill=tk.X, ipady=8)
        
        # Bind enter key to download
        self.url_entry.bind('<Return>', lambda event: self.on_download_click())
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="white")
        buttons_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Continue (Download) button
        self.download_btn = tk.Button(
            buttons_frame,
            text="Continue",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.on_download_click
        )
        self.download_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Get Info button
        self.info_btn = tk.Button(
            buttons_frame,
            text="Get Video Info",
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.on_get_info_click
        )
        self.info_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_btn = tk.Button(
            buttons_frame,
            text="Clear",
            font=("Arial", 12),
            bg="#FF5722",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.clear_input
        )
        self.clear_btn.pack(side=tk.LEFT)
        
        # Progress section
        progress_frame = tk.Frame(main_frame, bg="white")
        progress_frame.pack(fill=tk.X, pady=(30, 0))
        
        # Progress bar
        self.progress = ttk.Progressbar(
            progress_frame,
            mode='indeterminate',
            length=400
        )
        self.progress.pack(fill=tk.X, pady=(0, 10))
        
        # Progress label
        self.progress_label = tk.Label(
            progress_frame,
            textvariable=self.progress_var,
            font=("Arial", 10),
            bg="white",
            fg="#666666"
        )
        self.progress_label.pack()
        
        # Status section
        status_frame = tk.Frame(main_frame, bg="white")
        status_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Status label
        self.status_label = tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Arial", 12),
            bg="white",
            fg="#333333",
            wraplength=500,
            justify=tk.LEFT
        )
        self.status_label.pack(anchor=tk.W)
        
        # Initially hide progress
        self.hide_progress()
    
    def set_callbacks(self, download_callback: Callable, validate_url_callback: Callable, 
                     get_info_callback: Callable):
        """Set callback functions from controller"""
        self.download_callback = download_callback
        self.validate_url_callback = validate_url_callback
        self.get_info_callback = get_info_callback
    
    def on_download_click(self):
        """Handle download button click"""
        url = self.url_var.get().strip()
        if not url:
            self.show_error("Please enter a YouTube URL")
            return
        
        if self.validate_url_callback and not self.validate_url_callback(url):
            self.show_error("Please enter a valid YouTube URL")
            return
        
        # Start download in separate thread
        if self.download_callback:
            threading.Thread(target=self.download_callback, args=(url,), daemon=True).start()
    
    def on_get_info_click(self):
        """Handle get info button click"""
        url = self.url_var.get().strip()
        if not url:
            self.show_error("Please enter a YouTube URL")
            return
        
        if self.validate_url_callback and not self.validate_url_callback(url):
            self.show_error("Please enter a valid YouTube URL")
            return
        
        if self.get_info_callback:
            threading.Thread(target=self.get_info_callback, args=(url,), daemon=True).start()
    
    def clear_input(self):
        """Clear the URL input and reset UI"""
        self.url_var.set("")
        self.status_var.set("")
        self.progress_var.set("")
        self.hide_progress()
    
    def show_video_info_window(self, video_info: dict):
        """Show video information in a separate window"""
        try:
            VideoInfoWindow(self.root, video_info)
        except Exception as e:
            self.show_error(f"Error displaying video info: {str(e)}")
    
    def show_progress(self):
        """Show progress bar and start animation"""
        self.progress.pack(fill=tk.X, pady=(0, 10))
        self.progress.start(10)
        self.progress_label.pack()
    
    def hide_progress(self):
        """Hide progress bar and stop animation"""
        self.progress.stop()
        self.progress.pack_forget()
        self.progress_label.pack_forget()
    
    def update_progress(self, percent: str, speed: str):
        """Update progress information"""
        self.progress_var.set(f"Progress: {percent} | Speed: {speed}")
    
    def show_success(self, message: str):
        """Show success message"""
        self.status_var.set(f"✓ {message}")
        self.status_label.config(fg="#4CAF50")
        self.hide_progress()
    
    def show_error(self, message: str):
        """Show error message"""
        self.status_var.set(f"✗ {message}")
        self.status_label.config(fg="#F44336")
        self.hide_progress()
    
    def show_info_message(self, message: str):
        """Show info message"""
        self.status_var.set(f"ℹ {message}")
        self.status_label.config(fg="#2196F3")
    
    def disable_buttons(self):
        """Disable all buttons during operation"""
        self.download_btn.config(state=tk.DISABLED)
        self.info_btn.config(state=tk.DISABLED)
        self.clear_btn.config(state=tk.DISABLED)
    
    def enable_buttons(self):
        """Enable all buttons after operation"""
        self.download_btn.config(state=tk.NORMAL)
        self.info_btn.config(state=tk.NORMAL)
        self.clear_btn.config(state=tk.NORMAL)
    
    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()
    
    def destroy(self):
        """Destroy the GUI window"""
        self.root.destroy()
