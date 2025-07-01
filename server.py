import os

from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    mobile = request.form.get('mobile')
    username = request.form.get('username')
    profile = request.form.get('profile')
    amount = request.form.get('amount')
    upi = request.form.get('upi')
    utr = request.form.get('utr')
    payment_mode = request.form.get('payment_mode') or 'Not Provided'

    message = f'''
    New Payment Request:

    Mobile: {mobile}
    Instagram Username: {username}
    Profile Link: {profile}
    Amount: {amount}
    User UPI: {upi}
    UTR: {utr}
    Payment Mode: {payment_mode}
    '''

    sender_email = "2itzronak878@gmail.com"
    receiver_email = "2itzronak878@gmail.com"
    password = "gntrzqsehchervai"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New Payment Submission - Khelo India"

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {e}")

    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))