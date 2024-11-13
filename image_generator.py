from diffusers import StableDiffusionPipeline
import torch
from PIL import Image, ImageDraw, ImageFont

def create_good_morning_image():
    # Load the Stable Diffusion pipeline
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe = pipe.to("cuda") if torch.cuda.is_available() else pipe.to("cpu")

    # Define the prompt for generating the image
    prompt = "warm, affectionate image for person who loves books, spicy food, dogs, otters, kindness, and evergreen trees batik beaches.  "
    
    # Generate an image based on the prompt
    image = pipe(prompt).images[0]  # Generate the image

    # Save the generated image
    save_path = "good_afternoon_image.png"
    try:
        image.save(save_path)
        print(f"Image saved successfully at {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")



if __name__ == "__main__":
    create_good_morning_image()