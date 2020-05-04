# services/users/manage.py


import random
import string
import sys

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.users.models import Tweet, User, FollowRelationship

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_users(num_users):
    for _ in range(num_users):
        username = generate_random_string(6)
        user = User(username=username, email=f"{username}@gmail.com")
        db.session.add(user)


def create_tweets(num_tweets):
    users = User.query.all()
    for user in users:
        for _ in range(num_tweets):
            content = generate_random_string(140)
            tweet = Tweet(content=content, user_id=user.id)
            db.session.add(tweet)


def create_follow_relation():
    users = User.query.all()
    for user in users:
        if user.id != 1:
            follow = FollowRelationship(user_id=1, following_id=user.id)
            db.session.add(follow)
    

@cli.command("seed_db")
def seed_db():
    create_users(4)
    db.session.commit()
    create_tweets(4)
    db.session.commit()
    create_follow_relation()
    db.session.commit()


if __name__ == "__main__":
    cli()
