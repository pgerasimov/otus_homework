from webapp.model import app, db

with app.app_context():
    # Создаем таблицы в базе данных
    db.create_all()
