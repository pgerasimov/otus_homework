from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user, login_manager)

from webapp.forms import LoginForm, RegistrationForm
from webapp.model import db, Users, Posts
import logging

login_manager = LoginManager()


def load_user(user_id):
    # ваш код для получения пользователя по ID
    return Users.query.get(int(user_id))


login_manager.user_loader(load_user)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    logging.basicConfig(filename='app.log',
                        filemode='w',
                        level=logging.DEBUG,
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        format='%(name)s - %(levelname)s - %(message)s')

    login_manager.init_app(app)
    login_manager.login_view = 'login'

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

    @app.route("/contact")
    def contacts():
        title = "Контакты"
        return render_template('contact.html', page_title=title)

    @app.route('/post/<int:id>')
    def post(id):
        post = Posts.query.get(id)
        title = "Пост"
        return render_template('post.html', page_title=title, post=post)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            # пользователь уже авторизован, перенаправьте его, куда нужно
            return redirect(url_for('index'))

        form = LoginForm()

        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Вы успешно вошли в систему.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Неправильное имя пользователя или пароль.')

        return render_template("login.html", form=form, page_title="Авторизация")

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        user = Users.query.filter_by(email=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))

        else:
            flash('Неправильное имя пользователя или пароль')
            logging.error('Неправильное имя пользователя или пароль')
            return redirect(url_for('index'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно вышли из системы!')
        return redirect(url_for('index'))

    @app.route('/registration')
    def registration():
        if current_user.is_authenticated:
            flash('Вы уже авторизованы')
            return redirect(url_for('index'))

        title = "Регистрация"
        registration_form = RegistrationForm()
        return render_template(
            'register.html',
            page_title=title,
            form=registration_form,
            active='registration'
        )

    @app.route('/process_registration', methods=['POST'])
    def process_registration():

        form = RegistrationForm()

        if form.validate_on_submit():

            username = form.username_reg.data
            password = form.password_reg.data

            if Users.query.filter(Users.email == username).count():
                flash('Такой пользователь уже есть')
                logging.error('Такой пользователь уже есть')
                return redirect(url_for('registration'))

            new_user = Users(email=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            flash('Вы успешно зарегистрировались, можете авторизоваться')
            return redirect(url_for('index'))

        flash('Пароль не удовлетворяет требованиям. Повторите ввод')
        logging.error(
            'Форма не провалидировалась, Ошибка в пароле.')
        return redirect(url_for('registration'))

    return app
