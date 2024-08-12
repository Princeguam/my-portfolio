from flask import Flask, render_template, request, redirect
from db import *
import email_sender as es

app = Flask(__name__)


# Home route
@app.route('/')
@app.route('/index.html')
def home_page():
    return render_template('index.html')


# Dynamic Route
@app.route('/<string:dynamic>')
def random_page(dynamic):
    return render_template(dynamic)


# The filling of the contact form and the redirecting to a different file.
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    email = request.form.get('email')
    message = request.form.get('message')
    text = request.form.get('text')

    # save the data gotten from the form to the mongodb database
    data = Contact(
        email=email,
        text=text,
        message=message )
    data.save()

    # # This imports from the email_sender.py and sends an email to my gmail acct containing the data entered by the user
    # es.send_email(text, message, email)

    return redirect('/thankyou.html')

