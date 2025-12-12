import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import requests

load_dotenv()

def send_email_alert(subject, message):
    sender = os.getenv("ALERT_EMAIL")
    password = os.getenv("ALERT_EMAIL_PASSWORD")
    receiver = os.getenv("ALERT_RECEIVER")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))

    if not sender or not password or not receiver:
        print("⚠️ Missing email configuration in .env")
        return

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print(" Email alert sent successfully!")
    except Exception as e:
        print(f" Failed to send email alert: {e}")


def send_teams_alert(message):
    webhook_url = os.getenv("TEAMS_WEBHOOK_URL")
    if not webhook_url:
        print(" Teams webhook not configured.")
        return
    payload = {"text": message}
    try:
        requests.post(webhook_url, json=payload)
        print(" Teams alert sent successfully!")
    except Exception as e:
        print(f" Failed to send Teams alert: {e}")
