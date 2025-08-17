#!/usr/bin/env pwsh
# PowerShell script to run YouTube Video Downloader
# Developed by Malinda Prabath

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " YouTube Video Downloader" -ForegroundColor Yellow
Write-Host " Developed by Malinda Prabath" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to script directory
Set-Location $PSScriptRoot

# Check if virtual environment exists
if (Test-Path ".venv\Scripts\python.exe") {
    Write-Host "Using virtual environment..." -ForegroundColor Green
    & ".venv\Scripts\python.exe" launcher.py
} else {
    Write-Host "Using system Python..." -ForegroundColor Yellow
    python launcher.py
}

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Error occurred while running the application." -ForegroundColor Red
    Write-Host "Please check if all dependencies are installed." -ForegroundColor Yellow
    Write-Host "Run: pip install -r requirements.txt" -ForegroundColor Cyan
    Write-Host ""
    Read-Host "Press Enter to continue"
}

Read-Host "Press Enter to close"
