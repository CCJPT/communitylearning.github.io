# backend\images\image_gen.py

def generate_image(client, topic):
    prompt = f"Create an image or diagram of {topic}."

    # Change generate_image to generate_images
    response = client.models.generate_images(
        model="gemini-3-flash-image", # Use the flash image model
        prompt=prompt
    )

    # Note: response.generated_images is a list
    image = response.generated_images[0]
    
    # Save the image logic here...
    image_path = f"images/outputs/{topic.replace(' ', '_')}.png"
    image.image.save(image_path)
    return image_path