from mongoengine import *

class User(Document):
    name = StringField()
    phone = IntField()
    address = StringField()
    lat = StringField()
    lng = StringField()
    # coordinates = [FloatField(),FloatField()]

