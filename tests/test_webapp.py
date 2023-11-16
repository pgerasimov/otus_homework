from webapp.model import app, db, Users, Posts
import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def client():
    with app.app_context():
        db.create_all()

    yield client


def test_database_creation(client):
    with app.app_context():
        # Проверяем, что таблица Users существует
        assert 'users' in db.metadata.tables


def test_user_creation(client):
    # Проверяем, что пользователь создается
    with app.app_context():
        example_user = Users(email=fake.email())
        example_user.set_password(fake.password())
        db.session.add(example_user)
        db.session.commit()

        assert Users.query.filter_by(email=example_user.email).first() is not None


def test_duplicate_user_creation(client):
    # Проверяем, что нельзя создать пользователя с таким же email
    with app.app_context():
        example_user = Users(email=fake.email())
        example_user.set_password(fake.password())
        db.session.add(example_user)
        db.session.commit()

        duplicate_user = Users(email=example_user.email)
        duplicate_user.set_password(fake.password())

        with pytest.raises(Exception) as e_info:
            db.session.add(duplicate_user)
            db.session.commit()

        assert 'IntegrityError' in str(e_info.value)


def test_post_creation(client):
    # Проверяем, что пост создается
    with app.app_context():
        # Создаем тестового пользователя
        example_user = Users(email=fake.email())
        example_user.set_password(fake.password())
        db.session.add(example_user)
        db.session.commit()

        # Создаем тестовый пост
        example_post = Posts(
            post_title=fake.sentence(),
            post_image=fake.image_url(),
            post_summary=fake.paragraph(),
            post_content=fake.text(),
            post_rating=fake.random_int(min=1, max=5),
            author_id=example_user.id,
            publication_date=fake.date_time_this_decade(),
        )

        with app.test_request_context():
            db.session.add(example_post)
            db.session.commit()

        # Выводим все данные поста и его автора
        posts = Posts.query.all()
        for post in posts:
            print('\n')
            print(f"Post Title: {post.post_title}")
            print(f"Post Image: {post.post_image}")
            print(f"Post Summary: {post.post_summary}")
            print(f"Post Content: {post.post_content}")
            print(f"Post Rating: {post.post_rating}")
            author = Users.query.get(post.author_id)
            print(f"Author Email: {author.email}")
            print(f"Publication Date: {post.publication_date}")
            print("--------------------")
