# Two-Factor Authentication (2FA) Flask App

## Overview

This is a Flask-based web application that implements Two-Factor Authentication (2FA) using email and SMS. Users register with their contact information, log in with their credentials, and verify their identity using a One-Time Password (OTP) sent via email or SMS.

## Features

- User registration and login  
- OTP verification via email (SMTP) or SMS (Twilio)  
- Secure session management using Flask sessions  
- Flash messaging for user feedback  

## Requirements

Before running the application, install the dependencies:

```
pip install -r requirements.txt
```
Required Packages (from requirements.txt)
Flask
smtplib (built-in Python module)
twilio
Setup
Clone the repository:
```
git clone <repository-url>
cd <project-folder>
```
Configure environment variables:
Update the following placeholders in the script:
```
app.secret_key = 'your_secret_key'
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
verify_service_sid = 'your_verify_service_sid'
from_email = "your_email@gmail.com"
password = "your_email_password"
```
Ensure SMTP and Twilio credentials are correctly configured.

Run the application:
```
python app.py
```
Open your browser and go to:
```
http://127.0.0.1:5000/
```
## Usage
Register:
Create an account by providing a username, password, and contact information (email or phone number).
Login:
Enter your username and password.
OTP Verification:
If an email is provided, an OTP will be sent via email.
If a phone number (starting with +) is provided, an OTP will be sent via SMS using Twilio.
Access Success Page:
If the OTP is correct, the user is redirected to the success page.
Security Considerations
Use environment variables instead of hardcoding secrets in the code.
Implement brute-force protection for login attempts.
Secure email credentials using app passwords instead of personal passwords.
Enable HTTPS in production for secure communication.
