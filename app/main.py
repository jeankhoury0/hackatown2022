from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from app.controllers.GarbageController import getGarbageMessage
from app.controllers.UserController import UserController
from app.controllers.SmsController import SmsController
from flask_mongoengine import MongoEngine
from app.models.User import User
from dotenv import load_dotenv
load_dotenv()
import schedule
import time 


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine()
db.init_app(app)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        try:
            user_res = UserController.createUser(request)
            # todo fix this
            body_res = getGarbageMessage([-73.567031982444405, 45.490135392137702])
            print(user_res.phone, [user_res.lng, user_res.lat], body_res)
            newSMS = SmsController(user_res.phone, body_res)
            newSMS.sendSMS()
        except:
            return render_template('index.html')

    return render_template('index.html')

@app.route('/send-sms')
def send_sms():
    newSms = SmsController("+14385301370", "Hey Jean, n'oublie pas de sortir ta poubelle")
    sms = newSms.sendSMS()
    return sms.sid

@app.route('/get-garbage')
def get_garbage():
    coordinates = [-73.567031982444405, 45.490135392137702]
    return getGarbageMessage(coordinates)

    

if __name__ == '__main__':
    app.debug = True
    app.run()
