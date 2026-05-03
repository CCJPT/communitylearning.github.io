import os # OS module for file handling
from google import genai # Gemini API client
from svglib.svglib import svg2rlg # For converting SVG code to a renderable format
from reportlab.graphics import renderPM # For rendering to PNG
import io # For in-memory file handling

def generate_images(client, topic):

    prompt = f"""
    Write only the raw code for a detailed, colorful SVG diagram of {topic}. 
    Include clear labels for key parts. Use a white background.
    Ensure it is a complete <svg>...</svg> block.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Strip backticks for SVG code
    svg_content = response.text.replace("```svg", "").replace("```", "").strip()

    # Create folder for images if it doesn't exist
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save SVG and png file
    svg_path = f"{output_dir}/{topic.replace(' ', '_')}.svg"
    png_path = f"{output_dir}/{topic.replace(' ', '_')}.png"

    # Writes svg content to the disk
    with open(svg_path, "w", encoding="utf-8") as infile:
        infile.write(svg_content)

    # Convert SVG to PNG using svglib and reportlab
    # Return png or SVG if PNG generation fails
    try:
        drawing = svg2rlg(svg_path)
        renderPM.drawToFile(drawing, png_path, fmt="PNG")
        return png_path
    except Exception as e:
        print(f"Render Error: {e}")
        return svg_path 