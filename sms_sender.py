from twilio.rest import Client

# Replace these with your Twilio account credentials
ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

def send_sms(to, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        print(f"Message sent! ID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    recipient_number = input("Enter the recipient's phone number: ")
    message = "Good morning! Have a great day ahead!"
    send_sms(recipient_number, message)