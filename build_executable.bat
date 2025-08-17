@echo off
REM YouTube Video Downloader - Build Script
REM Creates a standalone executable for distribution
REM Developed by Malinda Prabath

echo ================================================================
echo  YouTube Video Downloader - Build Script
echo  Creating standalone executable for distribution
echo  Developed by Malinda Prabath
echo ================================================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install/upgrade build dependencies
echo Installing build dependencies...
pip install --upgrade pip
pip install -r requirements-dist.txt
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Clean previous builds
echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

REM Create executable
echo Creating standalone executable...
pyinstaller build_exe.spec --clean --noconfirm
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to create executable
    pause
    exit /b 1
)

REM Create installer directory
echo Creating installer package...
if not exist "installer" mkdir "installer"

REM Copy executable and required files
copy "dist\YouTube_Video_Downloader.exe" "installer\" >nul
copy "README.md" "installer\" >nul
copy "requirements.txt" "installer\" >nul

REM Create installation instructions
echo Creating installation instructions...
(
echo YouTube Video Downloader - Installation Instructions
echo =====================================================
echo.
echo 1. Copy YouTube_Video_Downloader.exe to your desired location
echo 2. Double-click YouTube_Video_Downloader.exe to run
echo 3. Enjoy downloading YouTube videos!
echo.
echo Features:
echo - Download YouTube videos up to 720p quality
echo - Smart playlist detection
echo - Professional user interface
echo - No Python installation required
echo.
echo Developed by Malinda Prabath
echo.
echo For support or issues, please contact the developer.
) > "installer\INSTALLATION_INSTRUCTIONS.txt"

echo.
echo ================================================================
echo  Build completed successfully!
echo.
echo  Files created in 'installer' folder:
echo  - YouTube_Video_Downloader.exe (Main application)
echo  - INSTALLATION_INSTRUCTIONS.txt (Setup guide)
echo  - README.md (Project information)
echo.
echo  You can now share the 'installer' folder with your friends!
echo ================================================================
echo.

pause
