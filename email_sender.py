import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

def send_email_with_image(image_path):
    # Setup server and login
    server = smtplib.SMTP('smtp.zoho.com', 587)
    server.starttls()
    server.login("blissful_life@zohomail.com", "Ld81FpHgE8mh")
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = "blissful_life@zohomail.com"
    msg['To'] = "evitarossi.budiawan@gmail.com"
    msg['Subject'] = "Good Morning!"
    
    # Email body
    body = "Wishing you a wonderful day ahead!"
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach image
    image_path = "good_morning_image.png"
    with open(image_path, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-Disposition', f'attachment; filename="{image_path}"')
        msg.attach(img)
    
    # Send email
    server.send_message(msg)
    server.quit()

# Call the function with the path to your generated image
send_email_with_image("generated_image.png")