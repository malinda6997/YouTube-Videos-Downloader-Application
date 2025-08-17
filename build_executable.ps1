#!/usr/bin/env pwsh
# YouTube Video Downloader - Build Script (PowerShell)
# Creates a standalone executable for distribution
# Developed by Malinda Prabath

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " YouTube Video Downloader - Build Script" -ForegroundColor Yellow
Write-Host " Creating standalone executable for distribution" -ForegroundColor Green
Write-Host " Developed by Malinda Prabath" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

# Change to script directory
Set-Location $PSScriptRoot

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to continue"
        exit 1
    }
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
if (Test-Path ".venv\Scripts\Activate.ps1") {
    & ".venv\Scripts\Activate.ps1"
} else {
    Write-Host "Warning: PowerShell activation script not found, using python directly" -ForegroundColor Yellow
}

# Install/upgrade build dependencies
Write-Host "Installing build dependencies..." -ForegroundColor Yellow
& python -m pip install --upgrade pip
& pip install -r requirements-dist.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}

# Clean previous builds
Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }
if (Test-Path "build") { Remove-Item -Recurse -Force "build" }

# Create executable
Write-Host "Creating standalone executable..." -ForegroundColor Yellow
& pyinstaller build_exe.spec --clean --noconfirm
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to create executable" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}

# Create installer directory
Write-Host "Creating installer package..." -ForegroundColor Yellow
if (-not (Test-Path "installer")) { New-Item -ItemType Directory -Name "installer" }

# Copy executable and required files
Copy-Item "dist\YouTube_Video_Downloader.exe" "installer\" -Force
Copy-Item "README.md" "installer\" -Force
Copy-Item "requirements.txt" "installer\" -Force

# Create installation instructions
Write-Host "Creating installation instructions..." -ForegroundColor Yellow
$instructions = @"
YouTube Video Downloader - Installation Instructions
=====================================================

1. Copy YouTube_Video_Downloader.exe to your desired location
2. Double-click YouTube_Video_Downloader.exe to run
3. Enjoy downloading YouTube videos!

Features:
- Download YouTube videos up to 720p quality
- Smart playlist detection
- Professional user interface
- No Python installation required

Developed by Malinda Prabath

For support or issues, please contact the developer.
"@

$instructions | Out-File -FilePath "installer\INSTALLATION_INSTRUCTIONS.txt" -Encoding UTF8

Write-Host ""
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Build completed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host " Files created in 'installer' folder:" -ForegroundColor Yellow
Write-Host " - YouTube_Video_Downloader.exe (Main application)" -ForegroundColor White
Write-Host " - INSTALLATION_INSTRUCTIONS.txt (Setup guide)" -ForegroundColor White
Write-Host " - README.md (Project information)" -ForegroundColor White
Write-Host ""
Write-Host " You can now share the 'installer' folder with your friends!" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

Read-Host "Press Enter to close"
