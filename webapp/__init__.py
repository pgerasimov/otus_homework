from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user)

from webapp.model import db, Users
import logging


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    db.init_app(app)
    migrate = Migrate(app, db)

    logging.basicConfig(filename='app.log',
                        filemode='w',
                        level=logging.ERROR,
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        format='%(name)s - %(levelname)s - %(message)s')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'registration'

    @app.after_request
    def add_header(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers['Cache-Control'] = 'public, max-age=0'
        return response

    @app.route("/")
    def index():
        return render_template('base.html', active='index')