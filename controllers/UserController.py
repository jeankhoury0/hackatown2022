from flask import jsonify
from models.User import User


class UserController():
    def createUser(req):
        user = User(name="jean")
        user.save()
        return jsonify(user.to_json())
