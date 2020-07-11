import flask
from flask import request, redirect

from cvAPP import app


@app.route("/")
def index():
    return flask.render_template("cvform.html")


@app.route("/submit-cv", methods=["GET", "POST"])
def build_cv():

    if request.method == "POST":
       if request.form['template'] == "1":
           return flask.render_template("cvoutput1.html", cv=request.form)
       if request.form['template'] == "2":
           return flask.render_template("cvoutput2.html", cv=request.form)

    return flask.render_template("cvform.html")
