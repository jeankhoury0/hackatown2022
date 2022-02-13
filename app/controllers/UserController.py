from flask import jsonify, flash, url_for, redirect
from app.controllers.GarbageController import getGarbageMessage
from app.models.User import User

#ImmutableMultiDict([('name', ''), ('phone', ''), ('address', '1245 Rue Notre-Dame Ouest, Montréal, Canada, H3C 6S3'), ('lat', '45.4935335'), ('lng', '-73.56458289999999')])

class UserController():
    def createUser(req):
        form = req.form
        print(form)

        if not req.form['name']:
            flash('Title is required!')
            return redirect(url_for('index'))
        
        user = User(name=req.form['name'], phone=req.form['phone'],
                    address=req.form['address'], lat=req.form['lat'], lng=req.form['lng'])
        #TODO add the options
        
        #TODO REMOVE
        # getGarbageMessage([req.form['lng'], req.form['lat']])
        getGarbageMessage([-73.567031982444405, 45.490135392137702])
        print("OK")
        user.save()
        return user
