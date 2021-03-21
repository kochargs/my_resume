from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__) # Initialize flask app
app.secret_key = 'super secret key'

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = "resume.gkochar@gmail.com"
app.config['MAIL_PASSWORD'] = "123!@#qweQWE"

mail = Mail(app)

from portfolio import routes
