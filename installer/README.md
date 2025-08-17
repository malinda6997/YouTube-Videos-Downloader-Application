# YouTube Video Downloader

A simple and elegant YouTube video downloader built with Python using MVC architecture.

## Features

- **Clean GUI Interface**: White background with intuitive design
- **MVC Architecture**: Well-organized code structure
- **Video Information**: Get detailed info about videos before downloading
- **Progress Tracking**: Real-time download progress and speed
- **Error Handling**: Comprehensive error messages and validation
- **Custom Download Path**: Choose where to save your videos

## Requirements

- Python 3.7 or higher
- yt-dlp library
- tkinter (usually comes with Python)

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Enter a YouTube URL in the text field
3. Click "Get Video Info" to see video details (optional)
4. Click "Continue" to start downloading
5. Videos will be saved to your Downloads/YouTube_Videos folder

## Project Structure

```
YouTube-Videos-Downloader-Application/
├── src/                     # Source code
│   ├── core/               # Business logic
│   │   ├── model.py        # Download engine
│   │   └── controller.py   # MVC controller
│   ├── ui/                 # User interface
│   │   ├── view.py         # Main GUI
│   │   └── splash.py       # Loading screen
│   └── utils/              # Utilities
│       └── config.py       # Configuration
├── tests/                  # Test files
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── main.py                 # Entry point
└── requirements.txt        # Dependencies
```

## MVC Architecture

- **Model** (`model.py`): Handles YouTube download logic using yt-dlp
- **View** (`view.py`): Manages the GUI interface with tkinter
- **Controller** (`controller.py`): Coordinates between Model and View

## Features Explanation

### GUI Components

- **Main Title**: "YouTube Video Downloader"
- **Input Field**: "Please enter your link"
- **Continue Button**: Starts the download process
- **Get Video Info Button**: Retrieves video information
- **Clear Button**: Clears input and resets interface
- **Progress Bar**: Shows download progress
- **Status Messages**: Success/error feedback

### Functionality

- URL validation for YouTube links
- Video information extraction
- High-quality video download (up to 720p)
- Progress tracking with speed information
- Automatic directory creation
- Error handling and user feedback

## Supported URL Formats

- https://www.youtube.com/watch?v=VIDEO_ID
- https://youtu.be/VIDEO_ID
- https://m.youtube.com/watch?v=VIDEO_ID

## Download Location

By default, videos are downloaded to:

- Windows: `C:\Users\[Username]\Downloads\YouTube_Videos\`
- macOS/Linux: `~/Downloads/YouTube_Videos/`

## Troubleshooting

1. **"Invalid YouTube URL"**: Make sure you're using a valid YouTube link
2. **Download fails**: Check your internet connection and try again
3. **Permission errors**: Make sure you have write permissions to the download folder

## Legal Notice

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download videos you have permission to download.

## License

This project is for personal use only.
