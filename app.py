from flask import Flask, render_template, request, redirect, url_for, session, flash
import smtplib
import random
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = 'your_secret_key'

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
verify_service_sid = 'your_verify_service_sid'
client = Client(account_sid, auth_token)

from_email = "your_email@gmail.com"
password = "your_email_password"
smtp_server = "smtp.gmail.com"
smtp_port = 587

users = {}

def send_email(to_email, otp):
    otp_str = str(otp)
    subject = "Your OTP Code"
    body = f"Your OTP is {otp_str}"
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(from_email, to_email, message)
    server.quit()

def send_otp_via_sms(phone_number):
    verification = client.verify \
        .v2 \
        .services(verify_service_sid) \
        .verifications \
        .create(to=phone_number, channel='sms')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        contact_info = request.form['username']
        users[username] = {'password': password, 'otp': None, 'contact_info': contact_info}
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            otp = random.randint(100000, 999999)
            users[username]['otp'] = otp
            
            contact_info = users[username]['contact_info']
            if contact_info.startswith('+'):
                send_otp_via_sms(contact_info)
            else:
                send_email(contact_info, otp)
            
            session['username'] = username
            return redirect(url_for('verify_otp'))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template('login.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        username = session.get('username')
        otp = request.form['otp']
        if username and 'otp' in users[username]:
            try:
                if users[username]['otp'] == int(otp):
                    return redirect(url_for('success'))
                else:
                    flash("Invalid OTP. Please try again.")
            except ValueError:
                flash("Invalid OTP. Please enter a numeric OTP.")
    return render_template('verify_otp.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
