# backend/text_gen.py

def generate_curriculum(client, topic):
    # This prompt is designed to get a structured, clean response
    prompt = f"""
    You are an expert educator. Create a structured curriculum for: {topic}.
    Include the following sections:
    - Overview: A high-level explanation.
    - Key Concepts: 3-5 essential bullet points.
    - Deep Dive: A detailed explanation of the mechanics.
    - Quick Quiz: 3 multiple-choice questions with answers.
    
    Use clear Markdown formatting.
    """

    try:
        # Using the model string verified by your curl command
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating text: {str(e)}"