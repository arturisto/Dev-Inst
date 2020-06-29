import flask


app = flask.Flask("TestApp")


@app.route('/Lesson')
def lesson():
    value = flask.Markup(open("in-this-chapter.md","r").read())
    return flask.render_template("Website.html", value=value,tab="lesson")


@app.route('/Exercise')
def exercise():

    value = flask.Markup(open("exercise.md","r").read())
    return flask.render_template("Website.html",value=value,tab="exe")


@app.route('/Home')
def home():
    return flask.render_template("Website.html",tab="home")


app.run()
