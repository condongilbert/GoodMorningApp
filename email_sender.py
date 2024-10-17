import smtplib

def send_email():
    # Setup server and login
    server = smtplib.SMTP('smtp.zoho.com', 587)
    server.starttls()
    server.login("blissful_life@zohomail.com", "Ld81FpHgE8mh")

    # Create email content
    subject = "Good Morning!"
    body = "Wishing you a wonderful day ahead!"
    message = f'Subject: {subject}\n\n{body}'

    # Send email
    server.sendmail("blissful_life@zohomail.com", "evitarossi.budiawan@gmail.com", message)
    server.quit()

send_email()