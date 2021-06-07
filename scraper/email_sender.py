import smtplib
from os import getenv
from email.mime.text import MIMEText


sender = "Private Person <from@example.com>"
receiver = "Private Person <from@example.com>"

def make_message(stock, action, price, user_email):
    message = MIMEText(format_message(stock, action, price, user_email))
    message["Subject"] = f"Alerta de {action}"
    message["From"] = sender
    message["To"] = user_email

    return message

def send_email(stock, action, price, user_email):
    email_message = make_message(stock, action, price, user_email)
    with smtplib.SMTP(getenv('EMAIL_HOST'), getenv('EMAIL_PORT')) as server:
        server.login(getenv('EMAIL_HOST_USER'), getenv('EMAIL_HOST_PASSWORD'))
        server.sendmail("from@example.com", "to@example.com ", email_message.as_string())
        


def format_message(stock, action, price, user_email):
    return f"""\
        Subject: Alerta de {action}
        To: to@example.com
        From: Private Person <>

        O preco de {price} alerta da acao {stock} foi atingido!
        Esta na hora de {action}."""