from . import db
from flask_login import UserMixin
from . import login_mgr
from sqlalchemy.orm import relationship


@login_mgr.user_loader
def user_loader(user_id):
    return Person.query.get(user_id)


class Person(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    name = db.Column(db.String(64))
    phone_number = db.Column(db.String(10))
    address = db.Column(db.String(64))
    nationality = db.Column(db.String(40), db.ForeignKey('tbl_nationality.nationality'))


class Tbl_nationality(db.Model, UserMixin):
    nationality = db.Column(db.String(40), primary_key=True)
    user_id = relationship("Person", backref="userid", lazy=True)
