from PIL import Image, ImageDraw, ImageFont
import os

# Print current working directory
print("Current working directory:", os.getcwd())

def create_simple_image():
    # Create a blank image with a solid color background
    img = Image.new('RGB', (800, 600), color=(255, 223, 186))
    draw = ImageDraw.Draw(img)

    message = "Good Morning, Beautiful!"
    font = ImageFont.truetype("arial.ttf", 40)
    text_bbox = draw.textbbox((0, 0), message, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    # Calculate the position to center the text
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
    
    # Draw the text
    draw.text(position, message, fill=(139, 0, 139), font=font)
    
    # Save the image in the same directory as the script
    save_path = "simple_image.png"
    try:
        img.save(save_path)
        print(f"Image saved successfully at {os.path.abspath(save_path)}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    create_simple_image()