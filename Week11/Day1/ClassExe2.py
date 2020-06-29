import flask

app = flask.Flask("TestApp")


@app.route('/space')
def view():
    html = flask.render_template("home.jin")
    return html



app.run()
