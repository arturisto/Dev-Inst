import os
import flask
from flask import request, flash, redirect, session
from . import app, db
from . import model

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


@app.route("/login_show")
def login_show():
    return flask.render_template("login.html")


@app.route("/login", methods=['POST', "GET"])
def login():
    # check if user in the DB:
    user = model.User.query.filter_by(username=request.form['username']).first()
    if user:
        if user.password == request.form['password']:
            session["user"] = user.username
            session['user_email'] = user.email
            flash("login complete, great success!")
            return flask.render_template("landing1.html", user=user)

        else:
            flask.flash("password is in correct")
            return flask.render_template("login.html")
    else:
        flask.flash("user doesn't exists, try again or sign in")
        return flask.render_template("login.html")


@app.route("/signin_show")
def signin_view():
    return flask.render_template("signin.html")


@app.route("/signin", methods=['POST', "GET"])
def signin():
    user = model.User.query.filter_by(email=request.form['email']).first()
    if user:
        if user.email == request.form['email']:
            flask.flash("email is taken, please use another")
        elif user.username == request.form['username']:
            flask.flash("username is taken, please use another")
    else:
        new_user = model.User(email=request.form['email'], password=request.form['password'],
                              username=request.form['username'])
        db.session.add(new_user)
        db.session.commit()
        return flask.render_template("landing1.html", user=user)

    return flask.redirect("/index")


@app.route("/signout", methods=['POST', "GET"])
def signout():
    session.clear()
    return flask.redirect("/index")


@app.route("/show")
def show_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'convert': 'USD',
        'id': '1,2,3,4'

    }
    headers = {
        'Accepts': 'application/json',
        'Accept-Encoding': 'deflate, gzip',
        'X-CMC_PRO_API_KEY': 'f187b324-e582-480e-8a40-5e360992424f'
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for key,value in data['data'].items():
            print(value['quote']['USD']['price'])

        return flask.render_template("index.html", data=data['data'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return flask.render_template("index.html")

