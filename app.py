import requests
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import time
import threading
import webbrowser

app = Flask(__name__)
socketio = SocketIO(app)

# A dictionary to store information for each generated email
email_data = {}

# Function to check for incoming emails for each generated email address


# def check_incoming_emails(email_login, email_domain):
#     shown_email_ids = set()  # Store seen email IDs for this email address

#     while True:
#         try:
#             # Check for new emails using the 1secmail API
#             url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={
#                 email_login}&domain={email_domain}"
#             response = requests.get(url)
#             emails = response.json()

#             if emails:
#                 for email in emails:
#                     email_id = email['id']

#                     # Only process emails that have not been shown yet
#                     if email_id not in shown_email_ids:
#                         subject = email['subject']
#                         from_email = email['from']

#                         # Add the email ID to the set of shown emails
#                         shown_email_ids.add(email_id)

#                         # Emit the new email details to the frontend
#                         socketio.emit('new_email', {
#                             'email_address': f"{email_login}@{email_domain}",
#                             'data': f"\nSender: {from_email}: \nSubject: {subject}"
#                         })
#         except Exception as e:
#             socketio.emit('new_email', {
#                 'email_address': f"{email_login}@{email_domain}",
#                 'data': f"Error fetching emails: {str(e)}"
#             })

#         time.sleep(5)  # Check for new emails every 5 seconds


# # Generate a new random email address using 1secmail API
# @app.route('/generate-email', methods=['POST'])
# def generate_email():
#     try:
#         url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
#         response = requests.get(url)
#         email_address = response.json()[0]
#         email_login, email_domain = email_address.split('@')

#         # Add the new email to the email_data dictionary
#         email_data[email_address] = {
#             'login': email_login,
#             'domain': email_domain
#         }

#         # Start checking for new emails for this email in a separate thread
#         thread = threading.Thread(
#             target=check_incoming_emails, args=(email_login, email_domain))
#         thread.start()

#         # Emit the new email address to the frontend
#         socketio.emit('new_email_address', {'email_address': email_address})

#     except Exception as e:
#         socketio.emit('new_email_address', {
#                       'email_address': f"Error generating email: {str(e)}"})

#     return jsonify({'status': 'Email generated'})

# Routing


@app.route('/')
def splash_screen():
    return render_template('index.html')  # Splash screen


@app.route('/email-generator')
def email_generator():
    return render_template('email_generator.html')  # Email generator page


@app.route('/image-resizer')
def image_resizer():
    return render_template('image_resizer.html')  # Image resizer page


@app.route('/regex-editor')
def regex_editor():
    return render_template('regex_editor.html')


if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    time.sleep(1)
    socketio.run(app)
