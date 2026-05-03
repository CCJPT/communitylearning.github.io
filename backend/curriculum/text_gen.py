def generate_curriculum(client, topic):

    prompt = f"""
    You are an expert educator. Create a structured curriculum for: {topic}.
    Include these sections:
    - Overview
    - Key Concepts (3-5 bullet points)
    - Deep Dive
    - Quick Quiz (3 multiple-choice questions with answers)

    Return clean HTML only using these tags:
    - <h2> for section titles
    - <ul><li> for bullet points
    - <strong> for key terms
    - <p> for paragraphs
    - <div class="concept-card"> to wrap each key concept bullet
    - <div class="quiz-section"> to wrap the entire quiz
    - <div class="quiz-question"> for each question
    - <div class="answer-key"> for the answer key

    No markdown. No backticks. No preamble. HTML only.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating text: {str(e)}"