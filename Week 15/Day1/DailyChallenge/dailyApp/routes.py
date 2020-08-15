import os
import flask
from flask import request, flash, redirect, session
from . import app, db
from . import model


@app.route("/index")
def home():
    return flask.render_template("/login.html")


@app.route("/login", methods=['POST', "GET"])
def login():
    # check if user in the DB:
    user = model.User.query.filter_by(email=request.form['email']).first()
    if "login" in request.form:
        if user:
            if user.password == request.form['password']:
                session["user"] = user.email
                if user.type == "admin":
                    return flask.render_template("landing1.html", user=user)
                else:
                    return flask.render_template("landing2.html", user=user)
            else:
                flask.flash("password is in correct")
                return flask.redirect("/index")
        else:
            flask.flash("user doesn't exists")
            return flask.redirect("/index")
    else:
        if user:
            if user.email == request.form['email']:
                flask.flash("email is taken, please use another")

        else:
            new_user = model.User(email=request.form['email'], password=request.form['password'],
                                  type=request.form['type'])
            db.session.add(new_user)
            db.session.commit()
            if request.form['type'] == "admin":
                return flask.render_template("landing1.html", user=user)
            else:
                return flask.render_template("landing2.html", user=user)
    return flask.redirect("/index")
@app.route("/singout")
def signout():
    pass
