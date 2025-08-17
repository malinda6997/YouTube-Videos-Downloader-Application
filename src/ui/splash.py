"""
Splash Screen module for YouTube Video Downloader
Shows loading screen with developer credits
"""

import tkinter as tk
from tkinter import ttk
import threading
import time


class SplashScreen:
    """Splash screen with loading animation and developer credits"""
    
    def __init__(self, duration=3000):
        self.duration = duration  # Duration in milliseconds
        self.splash = tk.Tk()
        self.splash.title("YouTube Video Downloader")
        self.splash.geometry("500x350")
        self.splash.configure(bg="#2C3E50")
        self.splash.resizable(False, False)
        
        # Remove window decorations
        self.splash.overrideredirect(True)
        
        # Center the splash screen
        self.center_window()
        
        # Create the UI
        self.setup_ui()
        
        # Start the loading animation
        self.start_loading()
    
    def center_window(self):
        """Center the splash screen on the screen"""
        self.splash.update_idletasks()
        width = self.splash.winfo_width()
        height = self.splash.winfo_height()
        x = (self.splash.winfo_screenwidth() // 2) - (width // 2)
        y = (self.splash.winfo_screenheight() // 2) - (height // 2)
        self.splash.geometry(f"{width}x{height}+{x}+{y}")
    
    def setup_ui(self):
        """Setup the splash screen UI"""
        # Main container
        main_frame = tk.Frame(self.splash, bg="#2C3E50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # App icon/logo area
        logo_frame = tk.Frame(main_frame, bg="#2C3E50")
        logo_frame.pack(pady=(20, 30))
        
        # App logo (using text as icon)
        logo_label = tk.Label(
            logo_frame,
            text="📺",
            font=("Arial", 48),
            bg="#2C3E50",
            fg="#E74C3C"
        )
        logo_label.pack()
        
        # App title
        title_label = tk.Label(
            main_frame,
            text="YouTube Video Downloader",
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        title_label.pack(pady=(0, 10))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Professional Video Download Solution",
            font=("Arial", 11),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Progress bar
        progress_frame = tk.Frame(main_frame, bg="#2C3E50")
        progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.progress = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            length=300,
            style='Custom.Horizontal.TProgressbar'
        )
        self.progress.pack()
        
        # Loading text
        self.loading_label = tk.Label(
            main_frame,
            text="Loading application...",
            font=("Arial", 10),
            bg="#2C3E50",
            fg="#95A5A6"
        )
        self.loading_label.pack(pady=(10, 0))
        
        # Developer credits
        credits_frame = tk.Frame(main_frame, bg="#2C3E50")
        credits_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(30, 0))
        
        # Developed by text
        developed_label = tk.Label(
            credits_frame,
            text="Developed by",
            font=("Arial", 9),
            bg="#2C3E50",
            fg="#7F8C8D"
        )
        developed_label.pack()
        
        # Developer name
        developer_label = tk.Label(
            credits_frame,
            text="Malinda Prabath",
            font=("Arial", 14, "bold"),
            bg="#2C3E50",
            fg="#3498DB"
        )
        developer_label.pack(pady=(2, 0))
        
        # Year
        year_label = tk.Label(
            credits_frame,
            text="© 2025",
            font=("Arial", 8),
            bg="#2C3E50",
            fg="#7F8C8D"
        )
        year_label.pack(pady=(5, 0))
        
        # Configure progress bar style
        self.setup_progress_style()
    
    def setup_progress_style(self):
        """Configure custom progress bar style"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'Custom.Horizontal.TProgressbar',
            background='#3498DB',
            troughcolor='#34495E',
            borderwidth=0,
            lightcolor='#3498DB',
            darkcolor='#3498DB'
        )
    
    def start_loading(self):
        """Start the loading animation"""
        self.progress['value'] = 0
        self.animate_progress()
    
    def animate_progress(self):
        """Animate the progress bar"""
        loading_steps = [
            (10, "Initializing components..."),
            (25, "Loading dependencies..."),
            (45, "Setting up environment..."),
            (65, "Configuring download engine..."),
            (80, "Preparing user interface..."),
            (95, "Finalizing setup..."),
            (100, "Ready to launch!")
        ]
        
        def update_progress(step_index=0):
            if step_index < len(loading_steps):
                progress_value, loading_text = loading_steps[step_index]
                
                # Update progress bar
                self.progress['value'] = progress_value
                
                # Update loading text
                self.loading_label.config(text=loading_text)
                
                # Update splash screen
                self.splash.update()
                
                # Schedule next update
                if step_index < len(loading_steps) - 1:
                    self.splash.after(400, lambda: update_progress(step_index + 1))
                else:
                    # Final step - close splash after short delay
                    self.splash.after(800, self.close_splash)
            
        # Start the animation
        update_progress()
    
    def close_splash(self):
        """Close the splash screen"""
        self.splash.destroy()
    
    def show(self):
        """Show the splash screen"""
        self.splash.mainloop()


def show_splash_screen(duration=3000):
    """Show splash screen and return when complete"""
    splash = SplashScreen(duration)
    splash.show()
