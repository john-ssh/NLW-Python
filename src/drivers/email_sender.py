import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_addrs, body):
    from_addr = "kmzmx5kqlru3nmjd@ethereal.email"
    login = "kmzmx5kqlru3nmjd@ethereal.email"
    password = "VF2AUNfgkJ5r8vbmDr"

    msg = MIMEMultipart()
    msg['From'] = "viagens_confirmar@email.com"
    msg['To'] = ", ".join(to_addrs)

    msg['Subject'] = "Confirmação de Viajem"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()