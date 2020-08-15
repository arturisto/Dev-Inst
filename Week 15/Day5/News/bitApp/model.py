from . import db
# from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import  ForeignKey




class User(db.Model):
    __tablename__ = "user"
    email = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

