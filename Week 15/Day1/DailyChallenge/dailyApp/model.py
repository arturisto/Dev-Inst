from . import db
from flask_login import UserMixin
from . import login_mgr

@login_mgr.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    email = db.Column(db.String(64), primary_key=True)
    password = db.Column(db.String(64))
    type = db.Column(db.String(5))

