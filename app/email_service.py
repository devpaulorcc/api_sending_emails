import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender, password_app, recipient, subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender = sender
    password = password_app
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    # Attach the message as plain text
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        
        server.sendmail(sender, recipient, msg.as_string())
        print("EMAIL SENT")
    except Exception as e:
        print(f"ERROR SENDING EMAIL: {e}")
    finally:
        server.quit()


