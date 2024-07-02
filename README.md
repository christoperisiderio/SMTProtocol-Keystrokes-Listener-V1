# SMTProtocol-Keystrokes Listener-V1
This simple project consists of two main components: a C program (main.c) that logs keystrokes and a Python script (SendEmail.pyw) that periodically emails the log file and a screenshot.
First time learning about socket, protocols, windows HHOOK, threading, etc.
Feel free to give an advice and insights for this project.

## Table of Contents
- Overview
- Files
- Dependencies
- Setup
- Usage
- Security Notice
### Overview
The keylogger listens for keyboard events and writes the keys pressed to a file. Additionally, it periodically emails this log file along with a screenshot of the current screen to a specified email address.

### Files
- main.c: The main C program that sets up a keyboard hook to log keystrokes and launches a background thread to send emails.
- SendEmail.pyw: A Python script that sends an email with the log file and a screenshot as attachments.
### Dependencies
1. Windows OS (for the keyboard hook and screenshot functionality)
2. Python 3.x
3. Python packages:
4. smtplib
5. dotenv
6. Pillow
7. A Gmail account for sending emails
   
### Setup
1. Compile main.c:
   ```bash
   gcc -o keylogger main.c -luser32

- NOTE: If you want to run it in background without showing the console use this instead:
   ```bash
   gcc -o main.exe main.c -luser32 -lgdi32 -lws2_32 -lwinmm -mwindows
 
2. Prepare the Python environment:
   Install required Python packages:
   ```bash
   pip install smtplib python-dotenv Pillow
3. Create a .env file in the same directory as SendEmail.pyw with your Gmail credentials:
   - GMAIL_EMAIL=your_email@gmail.com
   - GMAIL_APP_PASSWORD=your_app_password

5. makefile (optional, but recommended)

### Usage
6. Run the keylogger:
   ```bash
   ./keylogger

- The program will start logging keystrokes and sending emails every 10 seconds.

### Email Setup:
- The SendEmail.pyw script will run in the background, periodically sending emails to the specified recipient with the log file and a screenshot.

### Security Notice
> This project should be used responsibly and ethically. Unauthorized use of keyloggers can violate privacy and legal boundaries.
> Always obtain explicit consent from individuals before monitoring their activities.

### LICENSE
```sql
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


