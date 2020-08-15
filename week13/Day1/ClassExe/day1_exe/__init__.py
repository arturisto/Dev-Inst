import flask
import flask_sqlalchemy
import flask_migrate
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, 'learning_app.db')
app.config['SECRETKEY'] = "secretKey"
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

database_fn = "packages.json"
from . import routes
from . import model

