"""
Test file for YouTube Video Downloader
Simple tests to verify functionality
"""

import sys
import os

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from model import YouTubeDownloaderModel


def test_url_validation():
    """Test URL validation functionality"""
    model = YouTubeDownloaderModel()
    
    # Valid URLs
    valid_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://youtu.be/dQw4w9WgXcQ",
        "https://m.youtube.com/watch?v=dQw4w9WgXcQ"
    ]
    
    # Invalid URLs
    invalid_urls = [
        "https://www.google.com",
        "not_a_url",
        "",
        None,
        "https://vimeo.com/123456"
    ]
    
    print("Testing URL validation...")
    
    # Test valid URLs
    for url in valid_urls:
        result = model.validate_url(url)
        print(f"✓ {url}: {result}")
        assert result == True, f"Should be valid: {url}"
    
    # Test invalid URLs
    for url in invalid_urls:
        result = model.validate_url(url)
        print(f"✗ {url}: {result}")
        assert result == False, f"Should be invalid: {url}"
    
    print("URL validation tests passed!")


def test_model_initialization():
    """Test model initialization"""
    model = YouTubeDownloaderModel()
    
    assert hasattr(model, 'download_path'), "Model should have download_path attribute"
    assert os.path.exists(model.download_path), "Download directory should be created"
    
    print("Model initialization test passed!")


def run_tests():
    """Run all tests"""
    try:
        test_model_initialization()
        test_url_validation()
        print("\n🎉 All tests passed successfully!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
