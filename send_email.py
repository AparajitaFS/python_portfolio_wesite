import smtplib, ssl
import os


def send_email(message):
    print("os.getenv(MYPASSWORD)", os.getenv("MYPASSWORD"))
    host = "smtp.gmail.com"
    port = 465
    user = "test@gmail.com"
    password = os.getenv("MYPASSWORD")
    context = ssl.create_default_context()
    receiver = "test@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)
# send_email()