import random

from faker import Faker

from webapp import create_app
from webapp.model import Users, db, Posts

app = create_app()
fake = Faker()

with app.app_context():

    def generate_fake_user():
        email = fake.email()
        password = fake.password(length=12)
        date_registered = fake.date_time_this_decade()
        last_login = fake.date_time_this_year()

        user = Users(
            email=email,
            password=password,
            date_registered=date_registered,
            last_login=last_login
        )

        return user


    def generate_fake_post():
        title = fake.sentence()
        summary = fake.paragraph()
        content = "\n".join(fake.paragraph() for _ in range(3))
        rating = random.randint(1, 5)
        author_id = random.randint(1, 5)

        post = Posts(
            post_title=title,
            post_summary=summary,
            post_content=content,
            post_rating=rating,
            author_id=author_id
        )

        return post


    def populate_users_and_posts(num_users, num_posts_per_user):
        with app.app_context():
            for _ in range(num_users):
                user = generate_fake_user()
                db.session.add(user)
                db.session.commit()

                for _ in range(num_posts_per_user):
                    post = generate_fake_post()
                    post.author_id = user.id
                    db.session.add(post)
                    db.session.commit()


    populate_users_and_posts(5, 5)
