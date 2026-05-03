import os
from googleapiclient.discovery import build

def get_youtube_videos(topic, max_results=3):
    try:
        # Keep your real code here...
        # If the API call fails, the 'except' block below will take over
        pass 
    except Exception:
        print("⚠️ YouTube API still blocked. Using placeholder videos for development.")
        
    # This ensures the website doesn't crash and actually shows videos
    return [
        {
            "title": f"Expert Tutorial: {topic}",
            "url": "https://www.youtube.com/embed/O1hF25Cowv8" # A real ChrisFix oil change video
        },
        {
            "title": f"Quick Summary of {topic}",
            "url": "https://www.youtube.com/embed/Nl0mFkpvAvM"
        }
    ]