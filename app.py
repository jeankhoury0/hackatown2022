from flask import Flask, jsonify, render_template
from flask_mongoengine import MongoEngine
from models.User import User

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine()
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/')
def create():
    user = User(name="jean")
    user.save()
    return jsonify(user.to_json())
    

if __name__ == '__main__':
    app.debug = True
    app.run()
