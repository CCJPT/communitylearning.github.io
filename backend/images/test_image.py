import os
from google import genai
from dotenv import load_dotenv
from images.image_gen import generate_images

load_dotenv()
# Change your client setup to this:
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={'api_version': 'v1beta'} 
)

try:
    print("Generating image for 'Photosynthesis'...")
    path = generate_images(client, "Photosynthesis")
    print(f"Success! Image saved to: {path}")
except Exception as e:
    print(f"Error: {e}")