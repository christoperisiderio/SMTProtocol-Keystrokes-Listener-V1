# SMTProtocol-Keystrokes Listener-V1
This project consists of two main components: a C program (main.c) that logs keystrokes and a Python script (SendEmail.pyw) that periodically emails the log file and a screenshot.

This project consists of two main components: a C program (main.c) that logs keystrokes and a Python script (SendEmail.pyw) that periodically emails the log file and a screenshot.

# Table of Contents
> Overview
> Files
> Dependencies
> Setup
> Usage
> Security Notice
# Overview
The keylogger listens for keyboard events and writes the keys pressed to a file. Additionally, it periodically emails this log file along with a screenshot of the current screen to a specified email address.

# Files
> main.c: The main C program that sets up a keyboard hook to log keystrokes and launches a background thread to send emails.
> SendEmail.pyw: A Python script that sends an email with the log file and a screenshot as attachments.
# Dependencies
> Windows OS (for the keyboard hook and screenshot functionality)
> Python 3.x
> Python packages:
> smtplib
> dotenv
> Pillow
> A Gmail account for sending emails
# Setup
> Compile main.c:

# bash
> gcc -o keylogger main.c -luser32
# Prepare the Python environment:
> Install required Python packages:
# bash
> pip install smtplib python-dotenv Pillow
> Create a .env file in the same directory as SendEmail.pyw with your Gmail credentials:
> makefile (optional, but recommended)
> GMAIL_EMAIL=your_email@gmail.com
> GMAIL_APP_PASSWORD=your_app_password
# Usage
> Run the keylogger:

# bash
> ./keylogger
> The program will start logging keystrokes and sending emails every 10 seconds.

# Email Setup:
> The SendEmail.pyw script will run in the background, periodically sending emails to the specified recipient with the log file and a screenshot.

# Security Notice
> This project should be used responsibly and ethically. Unauthorized use of keyloggers can violate privacy and legal boundaries.
> Always obtain explicit consent from individuals before monitoring their activities.
