import flask
import requests
import mistune
from . import forms, models, create_user
from . import db
from . import login_manager
import flask_login  # LoginManager, login_user, login_required, logout_user, current_user
from flask import request, flash, redirect, session

main_blueprint = flask.Blueprint('main', __name__)


@main_blueprint.route('/', methods=['POST', 'GET'])
def index():
    """
    home page, shows the list of courses
    :return:
    """
    return flask.render_template('home.html')


# # ----------------------start of error routes------------------------------------#
@main_blueprint.route('/getout')
@login_manager.unauthorized_handler
def unauthorized():
    return "This place is not for you, please leave"

# # ----------------------End of error routes------------------------------------#
