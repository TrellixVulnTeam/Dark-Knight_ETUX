from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cf8684c33f10290611a8a2616c40efcc'  # Got using secrets.token_hex(16) from secrets module
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# after this import db in cmc
# then db.create_all() and then import User and Posts table and then use query

from flask_blog import routes
