from PIL import Image, ImageDraw, ImageFont

def create_good_morning_image():
    img = Image.new('RGB', (800, 600), color=(255, 223, 186))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)
    message = "Good Morning, Beautiful!"
    
    text_width, text_height = draw.textsize(message, font=font)
    position = ((img.width - text_width) // 2, (img.height - text_height) // 2)
    
    draw.text(position, message, fill=(139, 0, 139), font=font)
    img.save("good_morning_image.png")