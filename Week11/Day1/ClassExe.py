import flask

app = flask.Flask("TestApp")

@app.route('/space')
def view():
    html ="""
    hi there
        """
    return html

app.run()