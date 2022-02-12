from mongoengine import *

class User(Document):
    name = StringField()
    phone_number = IntField()
    address = StringField()
    coordinate = [FloatField(),FloatField()]
