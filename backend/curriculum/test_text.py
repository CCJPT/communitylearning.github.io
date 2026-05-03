import os
from google import genai
from dotenv import load_dotenv
from text_gen import generate_curriculum # Adjust if your filename is different

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def test_text():
    print("Generating curriculum for 'Photosynthesis'...")
    result = generate_curriculum(client, "Photosynthesis")
    print("\n--- GENERATED CONTENT ---")
    print(result)
    print("--------------------------")

if __name__ == "__main__":
    test_text()