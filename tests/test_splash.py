"""
Test the splash screen functionality
"""

import sys
import os

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from splash import show_splash_screen

def test_splash():
    """Test the splash screen with shorter duration"""
    print("Testing splash screen...")
    show_splash_screen(duration=2000)  # 2 seconds for testing
    print("Splash screen test completed!")

if __name__ == "__main__":
    test_splash()
