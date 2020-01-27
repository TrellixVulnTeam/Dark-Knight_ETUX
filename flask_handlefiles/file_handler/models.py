from datetime import datetime
from file_handler import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    profile_picture = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)


class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    file_name = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uploaded_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
