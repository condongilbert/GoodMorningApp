from PIL import Image, ImageDraw
import os

# Print current working directory
print("Current working directory:", os.getcwd())

def create_simple_image():
    # Create a blank image with a solid color background
    img = Image.new('RGB', (800, 600), color=(255, 223, 186))
    draw = ImageDraw.Draw(img)

    # Draw a simple rectangle or text
    draw.rectangle([50, 50, 750, 550], outline="purple", width=5)
    
    # Save the image in the same directory as the script
    save_path = "simple_image.png"
    try:
        img.save(save_path)
        print(f"Image saved successfully at {os.path.abspath(save_path)}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    create_simple_image()