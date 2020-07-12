from . import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    name = db.Column(db.String(64))
    phone_number = db.Column(db.String(10))
    address = db.Column(db.String(64))
