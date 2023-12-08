from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user)

from webapp.forms import LoginForm
from webapp.model import db, Users, Posts
import logging


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    logging.basicConfig(filename='app.log',
                        filemode='w',
                        level=logging.DEBUG,
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        format='%(name)s - %(levelname)s - %(message)s')

    @app.after_request
    def add_header(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response

    @app.errorhandler(500)
    def internal_server_error(e):
        return f'Internal Server Error: {str(e)}', 500

    @app.route("/")
    def index():
        all_posts = Posts.query.all()
        title = "Главная страница"
        return render_template('main.html', page_title=title, posts=all_posts, active='index')

    return app
