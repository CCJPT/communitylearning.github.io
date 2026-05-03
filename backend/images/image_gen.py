import os
from google import genai
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import io

def generate_images(client, topic):
    # 1. Ask the free text model to write SVG code
    prompt = f"""
    Write only the raw code for a detailed, colorful SVG diagram of {topic}. 
    Include clear labels for key parts. Use a white background.
    Ensure it is a complete <svg>...</svg> block.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # 2. Extract the SVG code (clean up any markdown backticks)
    svg_content = response.text.replace("```svg", "").replace("```", "").strip()

    # 3. Ensure output directory exists
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 4. Save SVG and Render to PNG
    svg_path = f"{output_dir}/{topic.replace(' ', '_')}.svg"
    png_path = f"{output_dir}/{topic.replace(' ', '_')}.png"

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    # Use svglib to convert SVG to a drawing, then render to PNG
    try:
        drawing = svg2rlg(svg_path)
        renderPM.drawToFile(drawing, png_path, fmt="PNG")
        return png_path
    except Exception as e:
        print(f"Render Error: {e}")
        return svg_path  # Fallback to the SVG file if PNG fails