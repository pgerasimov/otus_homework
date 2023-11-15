from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(120))
    date_registered = db.Column(db.DateTime, default=datetime.datetime.now)
    last_login = db.Column(db.DateTime, default=datetime.datetime.now)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(120))
    post_image = db.Column(db.String(120), nullable=True)
    post_summary = db.Column(db.String(600), nullable=True)
    post_content = db.Column(db.String(1200), nullable=True)
    post_rating = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    publication_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String(1200))
    post_id = db.Column(db.Integer, db.ForeignKey('Posts.id'))


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(20))
    post_id = db.Column(db.Integer, db.ForeignKey('Posts.id'))

