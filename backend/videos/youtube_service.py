import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

def get_youtube_videos(topic, max_results=3):
    api_key = os.getenv("YOUTUBE_API_KEY")
    
    try:
        # Build the YouTube service
        youtube = build("youtube", "v3", developerKey=api_key)
        
        # Search for educational videos
        search_query = f"{topic} educational tutorial"
        
        request = youtube.search().list(
            q=search_query,
            part="snippet",
            maxResults=max_results,
            type="video",
            videoEmbeddable="true"
        )
        response = request.execute()

        videos = []
        for item in response.get("items", []):
            video_id = item["id"]["videoId"]
            videos.append({
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/embed/{video_id}",
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"]
            })
        
        return videos

    except Exception as e:
        print(f"❌ YouTube API Error: {e}")
        return []

if __name__ == "__main__":
    # Quick Test
    print("🚀 Testing New YouTube Key...")
    results = get_youtube_videos("How to bake a cake")
    for v in results:
        print(f"Found: {v['title']}")