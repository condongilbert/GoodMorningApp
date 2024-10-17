import smtplib

def send_email():
    # Setup server and login
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("blissful_life@zohomail.com", "pbRc6GnMvDsv")

    # Create email content
    subject = "Good Morning!"
    body = "Wishing you a wonderful day ahead!"
    message = f'Subject: {subject}\n\n{body}'

    # Send email
    server.sendmail("blissful_life@zohomail.com", "condongilbert@gmail.com", message)
    server.quit()

send_email()