from email.message import EmailMessage
from os import getenv
from dotenv import load_dotenv
import smtplib
import ssl

# email name is the email of the person filling out the contact form.

load_dotenv()

def send_email(subject, body, email_name):
    email_sender = getenv("EMAIL_SENDER")
    email_receiver = getenv('EMAIL_RECEIVER')
    email_password = getenv('EMAIL_PASSWORD')

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em['by'] = email_name
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtps:
        smtps.login(email_sender, email_password)
        smtps.sendmail(email_sender, email_receiver, email_name, em.as_string())
