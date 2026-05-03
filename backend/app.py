import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

# Import your custom modules
from curriculum.text_gen import generate_curriculum
from images.image_gen import generate_images
from videos.video_gen import generate_video

load_dotenv()
app = Flask(__name__)
CORS(app)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/api/generate-all', methods=['POST'])
def generate_all():
    data = request.json
    topic = data.get('topic')

    # Run all three features!
    text_path = generate_curriculum(client, topic)
    img_path = generate_images(client, topic)
    vid_path = generate_video(client, topic)

    return jsonify({
        "curriculum": text_path,
        "image_url": img_path,
        "video_url": vid_path
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)