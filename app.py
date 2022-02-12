from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from controllers.UserController import UserController
from controllers.SmsController import SmsController
from flask_mongoengine import MongoEngine
from models.User import User
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine()
db.init_app(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        res = UserController.createUser(request)
        
    return render_template('index.html')

@app.route('/send-sms')
def send_sms():
    newSms = SmsController("+14385301370", "Hey Jean, n'oublie pas de sortir ta poubelle")
    sms = newSms.sendSMS()
    return sms.sid



if __name__ == '__main__':
    app.debug = True
    app.run()
