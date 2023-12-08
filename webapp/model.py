from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.datetime.now)
    last_login = db.Column(db.DateTime, default=datetime.datetime.now)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.email}>'

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(120), nullable=False)
    post_image = db.Column(db.String(120), nullable=True)
    post_summary = db.Column(db.String(600), nullable=True)
    post_content = db.Column(db.String(1200), nullable=True)
    post_rating = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    publication_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String(1200), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(20), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)




