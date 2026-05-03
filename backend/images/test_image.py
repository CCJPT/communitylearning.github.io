import os
import sys
from google import genai
from dotenv import load_dotenv

# Ensure we are pointing at the correct .env (parent folder)
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Verify API key is loading
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    sys.exit("Error: GEMINI_API_KEY not found in .env")

# Initialize client (defaults to v1beta)
client = genai.Client(api_key=api_key)

# Local import fix (ensures image_gen is found)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from image_gen import generate_images

def run_test():
    topic = "Image of how to repair a car tire"
    print(f"🧠 'Text First' visual test for: {topic}")
    print("---------------------------------------")
    
    try:
        # Calls our new text-based generator
        saved_path = generate_images(client, topic)
        print(f"✅ Success! Free 'visual' saved to: {saved_path}")
        
        print("\n--- GENERATED VISUAL ---")
        with open(saved_path, 'r') as f:
            print(f.read())
        print("--------------------------")
        
    except Exception as e:
        print(f"❌ Error during test: {e}")

if __name__ == "__main__":
    run_test()