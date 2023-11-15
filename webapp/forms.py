from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Regexp, EqualTo

regexp = r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z\S+]{8,}'


class LoginForm(FlaskForm):
    username = StringField(
        'Email',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter email",
            "type": "email"})
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter Password",
            "type": "password"})
    submit = SubmitField(
        'Войти',
        render_kw={
            "class": "btn btn-primary",
            "Type": "submit"})
    remember_me = BooleanField(
        'Запомнить меня',
        default=True,
        render_kw={"class": "form-check-input"})


class RegistrationForm(FlaskForm):
    username_reg = StringField(
        'Email',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter email",
            "type": "email"})
    password_reg = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Regexp(regexp)
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter Password",
            "type": "password"})
    password_reg_confirm = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Regexp(regexp),
            EqualTo('password_reg')
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter Password",
            "type": "password"})
    submit_reg = SubmitField(
        'Зарегистрироваться',
        render_kw={
            "class": "btn btn-primary",
            "Type": "submit"})