from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '27f54a12c5b50d834dcd5e2ff2afa10d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from election_app import routes
