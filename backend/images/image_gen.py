# backend/images/image_gen.py

def generate_images(client, topic):
    prompt = f"An educational diagram of {topic}, clear labels, high resolution."

    # Change the model string to this exact version:
    response = client.models.generate_images(
        model="Imagen-3-flash-image",
        prompt=prompt
    )

    image = response.generated_images[0]
    
    # Ensure the directory exists before saving
    output_dir = "images/outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_path = f"{output_dir}/{topic.replace(' ', '_')}.png"
    image.image.save(image_path)
    return image_path