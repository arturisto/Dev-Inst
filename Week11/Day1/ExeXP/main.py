import flask
import json

app = flask.Flask("TestApp")


@app.route('/Home')
def home():
    workplaces_json = json.load(open("workplaces.json", "r"))
    return flask.render_template("index.html", workplaces=workplaces_json['workplaces'],
                                 personal=workplaces_json['personal_data'],
                                 education=workplaces_json['education'], software=workplaces_json['software'],
                                 image=workplaces_json['image'])


app.run()
