# КОД ДЛЯ ДОШМАНЕГО ЗАДАНИЯ. Выбираем пользователя из БД

from webapp import Users
from webapp.model import app

with app.app_context():
    selected_users = Users.query.filter(Users.id < 10).all()

    for user in selected_users:
        print(f"User ID: {user.id}, Email: {user.email}")
