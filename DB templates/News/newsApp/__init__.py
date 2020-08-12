import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, 'learning_app.db')
app.config['SECRET_KEY'] = "secretKey"
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
login_mgr = flask_login.LoginManager(app)

database_fn = "packages.json"
from . import views,model
db.create_all()
