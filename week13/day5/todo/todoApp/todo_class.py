from . import db
import sqlalchemy
from . import model


class Todo():

    def __init__(self, todo=None):
        self.todo_text = todo

    def get_todo_list(self):
        return model.Todo_list.query.all()

    def save_todo(self, form):
        my_model = model.Todo_list(todo=self.todo_text)
        category = model.Category(name=form['category'])
        my_model.category.append(category)
        db.session.add(my_model)
        db.session.flush()
        img = model.Image(image=form['Image'], todo_id=my_model.id)
        db.session.add(img)
        db.session.commit()

    def complete_task(self, id):
        db.session.query(model.Todo_list).filter(model.Todo_list.id == id).update({"is_complete": True})
        db.session.commit()
