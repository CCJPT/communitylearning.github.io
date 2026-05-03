def generate_video(client, topic):
    prompt = f"Create example videos teaching {topic}."
    
    # Veo generates high-fidelity video with audio
    operation = client.models.generate_video(
        model="veo-3-generate",
        prompt=prompt
    )

    result = operation.result() 
    video_path = f"video/outputs/{topic.replace(' ', '_')}.mp4"
    result.video.save(video_path)
    return video_path