import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("--- AVAILABLE MODELS ---")
try:
    for model in client.models.list():
        # Just printing the model object to see everything it contains
        print(f"Name: {model.name}")
        # If you want to see methods, try this attribute:
        if hasattr(model, 'supported_methods'):
            print(f"  Methods: {model.supported_methods}")
except Exception as e:
    print(f"Error: {e}")