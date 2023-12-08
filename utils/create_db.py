from utils.fake_db_data import populate_users_and_posts
from webapp.model import app, db

with app.app_context():
    # Создаем таблицы в базе данных
    db.create_all()

    populate_users_and_posts(5, 5)
