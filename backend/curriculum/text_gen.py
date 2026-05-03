def generate_learning_path(client, topic):
    prompt = f"Create a curriculum for {topic}."
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text