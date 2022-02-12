from flask import jsonify
from models.User import User

#ImmutableMultiDict([('name', ''), ('phone', ''), ('address', '1245 Rue Notre-Dame Ouest, Montréal, Canada, H3C 6S3'), ('lat', '45.4935335'), ('lng', '-73.56458289999999')])

class UserController():
    def createUser(req):
        form = req.form
        user = User(name=req.form['name'], phone=req.form['phone'],
                    address=req.form['address'], lat=req.form['lat'], lng=req.form['lng'])
        #TODO add the options
        user.save()
        return jsonify(user.to_json())
