import os # For environment variable handling
from dotenv import load_dotenv # To load environment variables from a .env file
from googleapiclient.discovery import build # To interact with the YouTube Data API

# Load environment variables
load_dotenv()

def get_youtube_videos(topic, max_results=3):
    api_key = os.getenv("YOUTUBE_API_KEY")
    
    try:
        # Build the YouTube service
        youtube = build("youtube", "v3", developerKey=api_key)
        
        # Search for educational videos
        search_query = f"{topic} educational tutorial"
        
        # Make the API request to search for videos
        request = youtube.search().list(
            q=search_query,
            part="snippet",
            maxResults=max_results,
            type="video",
            videoEmbeddable="true"
        )
        response = request.execute()

        # Process the response to extract video details
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