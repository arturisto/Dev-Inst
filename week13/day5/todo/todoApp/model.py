from . import db

category_to_item = db.Table("categories_identifier",
                            db.Column("todo_id", db.Integer, db.ForeignKey("todo_list.id")),
                            db.Column("category_id", db.Integer, db.ForeignKey("categories.id")))


class Todo_list(db.Model):
    __tablename__ = "todo_list"
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200))
    is_complete = db.Column(db.Boolean, default=False)
    image = db.relationship("Image", uselist=False, back_populates='action_item')
    category = db.relationship("Category", secondary=category_to_item)


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200))
    todo_id = db.Column(db.Integer, db.ForeignKey("todo_list.id"))
    action_item = db.relationship("Todo_list", back_populates="image")
