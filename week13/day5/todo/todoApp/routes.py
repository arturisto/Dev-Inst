import os
import flask
from flask import request, flash, redirect, session
from . import app, db
from . import model
from .todo_class import Todo


@app.route("/home")
def index():
    todo = Todo()

    return flask.render_template("index.html", todo_list=todo.get_todo_list())


@app.route("/add_todo", methods=['POST', 'GET'])
def add_todo():
    todo_item = Todo(request.form['todo'])
    todo_item.save_todo(request.form)

    return redirect('/home')


@app.route("/complete/<int:todo_id>", methods=['POST', 'GET'])
def complete_todo(todo_id):
    todo = Todo()
    print(todo_id)
    todo.complete_task(todo_id)
    return redirect('/home')

