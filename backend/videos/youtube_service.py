import os
from googleapiclient.discovery import build

def get_youtube_videos(topic, max_results=3):
    # Uses the same Google Cloud Project API Key
    api_key = os.getenv("GEMINI_API_KEY") 
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        q=f"{topic} educational tutorial",
        part="id,snippet",
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
            "url": f"https://www.youtube.com/embed/{video_id}"
        })
    return videos