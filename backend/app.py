import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai  
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/api/generate', methods=['POST'])

def generate():
    data = request.json
    user_topic = data.get('topic', 'content')

    prompt = f"Create a learning module for: {user_topic}. Be concise and professional. Include key points, examples, and a summary."

    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=prompt
    )

    return jsonify({
        "status": "success",
        "curriculum": response.text
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)