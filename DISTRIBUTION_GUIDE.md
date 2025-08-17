# YouTube Video Downloader - Distribution Guide

## 📦 Creating Standalone Desktop Application

This guide helps you create a distributable version of the YouTube Video Downloader that your friends can install and run without needing Python.

### 🛠️ Build Process

#### Option 1: Using Batch Script (Windows)
```cmd
build_executable.bat
```

#### Option 2: Using PowerShell Script
```powershell
.\build_executable.ps1
```

#### Option 3: Manual Build
```cmd
# Install dependencies
pip install -r requirements-dist.txt

# Create executable
pyinstaller build_exe.spec --clean --noconfirm
```

### 📁 Output Files

After building, you'll find these files in the `installer/` folder:

- **`YouTube_Video_Downloader.exe`** - Main application (standalone)
- **`INSTALLATION_INSTRUCTIONS.txt`** - Setup guide for users
- **`README.md`** - Project documentation

### 🚀 Distribution

#### For Your Friends:
1. **Zip the `installer` folder**
2. **Share the zip file** via email, cloud storage, or USB
3. **They extract and run** `YouTube_Video_Downloader.exe`

#### Requirements for Users:
- ✅ **Windows 10/11** (any version)
- ✅ **No Python installation needed**
- ✅ **No additional software required**
- ✅ **Internet connection** (for downloading videos)

### 📝 Features Included

- ✅ YouTube video downloading (up to 720p)
- ✅ Smart playlist detection
- ✅ Professional splash screen
- ✅ Error handling and user guidance
- ✅ Copy video information feature
- ✅ Custom download paths

### 🔧 Customization Options

#### Adding an Icon:
1. Create or find a `.ico` file
2. Place it in the project root
3. Update `build_exe.spec` line: `icon='your_icon.ico'`

#### Changing App Name:
Update the `name` field in `build_exe.spec`:
```python
name='Your_Custom_Name'
```

### 📊 File Sizes

- **Executable size**: ~50-80 MB (includes Python runtime and all dependencies)
- **Startup time**: 3-5 seconds (first launch may be slower)
- **Memory usage**: ~50-100 MB when running

### 🐛 Troubleshooting

#### If build fails:
1. Ensure Python 3.8+ is installed
2. Run: `pip install --upgrade pyinstaller`
3. Check antivirus isn't blocking the build
4. Try running as administrator

#### If executable doesn't run:
1. Check Windows Defender/antivirus settings
2. Ensure all files are in the same folder
3. Run from command prompt to see error messages

### 📤 Sharing Methods

#### Email (Small Groups):
- Zip the installer folder
- Send via email (check size limits)

#### Cloud Storage (Recommended):
- Upload to Google Drive/OneDrive/Dropbox
- Share download link

#### USB/External Drive:
- Copy installer folder directly
- No compression needed

#### GitHub Releases:
- Create a release on your GitHub repository
- Upload the installer as release assets

### 🔐 Security Notes

- The executable is **safe and clean**
- Some antivirus may flag it (false positive)
- Users may need to **"Allow"** or **"Trust"** the application
- Consider code signing for professional distribution

### 💡 Pro Tips

1. **Test thoroughly** before sharing
2. **Include clear instructions** for your friends
3. **Provide your contact** for support
4. **Consider creating a demo video** showing how to use it

---

**Developed by Malinda Prabath**  
*Share your YouTube Video Downloader with confidence!*
