from youtube_service import get_youtube_videos
import os
from dotenv import load_dotenv

load_dotenv()

def test_api():
    print("🚀 Testing YouTube Integration...")
    try:
        results = get_youtube_videos("How to change car oil")
        for i, vid in enumerate(results):
            print(f"Video {i+1}: {vid['title']}")
            print(f"   URL: {vid['url']}")
        print("✅ API Test Passed!")
    except Exception as e:
        print(f"❌ API Test Failed: {e}")

if __name__ == "__main__":
    test_api()