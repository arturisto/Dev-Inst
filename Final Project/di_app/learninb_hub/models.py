import datetime
import flask_sqlalchemy
import jwt
from flask_login import UserMixin
from flask_mail import Message
from .. import db, login_manager, mail_manager
import flask
from flask import current_app



class Questions(db.Model):
    pass

class Exams(db.Model):
    pass

class Notions(db.Model):
    pass

class subNotions(db.Model):
    pass