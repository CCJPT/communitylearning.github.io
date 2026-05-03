import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("--- Available Models ---")
# This lists all models available to your specific API key
for model in client.models.list():
    print(f"Name: {model.name}")
    print(f"Supported Actions: {model.supported_generation_methods}")
    print("-" * 20)