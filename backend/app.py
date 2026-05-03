import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

# Import your custom modules
from curriculum.text_gen import generate_curriculum
from images.image_gen import generate_images
from videos.youtube_service import get_youtube_videos # New Import

load_dotenv()
app = Flask(__name__, 
            template_folder='../frontend/pages', 
            static_folder='../frontend/styles')  
CORS(app)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# --- PAGE ROUTES (To open the files in browser) ---

@app.route('/')
def index():
    """Opens the homepage"""
    return render_template('homepage.html')

@app.route('/customlearning.html')
def learning_page():
    """Opens the learning dashboard"""
    return render_template('customlearning.html')

# API ROUTES (AI GENERATION)
@app.route('/api/generate-all', methods=['POST'])
def generate_all():
    data = request.json
    topic = data.get('topic')

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    try:
        # 1. Generate AI Curriculum & Image
        text_content = generate_curriculum(client, topic)
        img_path = generate_images(client, topic)
        
        # 2. Get YouTube Videos
        video_list = get_youtube_videos(topic)

        return jsonify({
            "topic": topic,
            "curriculum": text_content,
            "image_url": img_path,
            "videos": video_list
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)