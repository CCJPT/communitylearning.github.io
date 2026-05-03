import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

# Import your custom modules
from curriculum.text_gen import generate_curriculum
from images.image_gen import generate_images
from videos.youtube_service import get_youtube_videos # New Import

load_dotenv()
app = Flask(__name__)
CORS(app)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/api/generate-all', methods=['POST'])
def generate_all():
    data = request.json
    topic = data.get('topic')

    # 1. Generate text and images locally/via Gemini
    text_content = generate_curriculum(client, topic)
    img_path = generate_images(client, topic)
    
    # 2. Get real YouTube embed links instead of generating a file
    video_list = get_youtube_videos(topic)

    return jsonify({
        "curriculum": text_content,
        "image_url": img_path,
        "videos": video_list # Returns a list of titles and embed URLs
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)