from portfolio import app, mail, Message
from flask import render_template, request, url_for, redirect, flash
import json


with open('portfolio/templates/config.json') as f:
    params = json.load(f)['params']


def send_email():
   name = request.form['Name']
   email = request.form['Email']
   message = request.form['Message']
   msg = Message(subject = f'Heroku Resume - {name}', sender = email, recipients = ["kochar.gurpreet@gmail.com"], cc = [email])
   msg.body = message
   mail.send(msg)
   if name and email and message:
         flash("Thank you for contacting me. I will get back to you soon.")


@app.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
      send_email()
   return render_template('index.html', params=params)


@app.route('/project/<project>')
def project_details(project):
   return render_template('project_details.html', params=params, project=project)
