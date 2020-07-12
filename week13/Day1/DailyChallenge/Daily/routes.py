import os
import flask
from flask import request, flash, redirect, session
from . import app, db
from . import model


@app.route("/add")
def add_user_page():
    return flask.render_template("add_user.html")


@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        form = request.form
        mymodel = model.Person(name=form['name'], email=form['email'], phone_number=form['phone number'],
                               address=form['Address'])
        db.session.add(mymodel)
        db.session.commit()

    return redirect("/add")


@app.route("/find")
def find():
    return flask.render_template("show_user.html")


@app.route("/find_user", methods=['POST', 'GET'])
def find_user():
    if request.method == 'POST':
        form = request.form

        if len(form['name']) > 0:
            person = model.Person.query.filter_by(name=form['name']).first()
        else:
            person = model.Person.query.filter_by(phone_number=form['phone number']).first()
        msg = f'name:{person.name}, address:{person.address}'
        flash(msg)
        print(person)


    return redirect("/find")
