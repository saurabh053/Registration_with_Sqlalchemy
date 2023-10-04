from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = 'thisisthefirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/cjflask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app)

from code_jana import routes
