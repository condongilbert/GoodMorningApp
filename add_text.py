from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, output_path):
    # Open the generated image
    image = Image.open(image_path)

    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)

    # Load a font (use a TTF font you have or download one)
    font = ImageFont.truetype("arial.ttf", 20)

    # Define the position and text color
    text_position = (50, 50)
    text_color = (255, 255, 255)  # White

    # Add text to the image
    draw.text(text_position, text, font=font, fill=text_color)

    # Save the edited image
    image.save(output_path)
    print(f"Image saved with text at {output_path}")

# Example usage
add_text_to_image("good_morning_image.png", "Get some rest today beautiful!!", "good_morning_with_text.png")