from . import db


class Todo_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200))
    is_complete = db.Column(db.Boolean, default=False)
