# services/users/project/api/users/crud.py


from project import db
from project.api.users.models import User, Tweet, FollowRelationship

from flask_sqlalchemy import SQLAlchemy

def get_time_line(user_id):  # To simplify, assume the user followed every one
    follow_relationships = FollowRelationship.query.filter_by(user_id=user_id).all()
    following_user_ids = [follow.following_id for follow in follow_relationships]
    return Tweet.query.filter(Tweet.user_id.in_(following_user_ids)).all()


def get_all_users():
    return User.query.all()


def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user, username, email):
    user.username = username
    user.email = email
    db.session.commit()
    return user


def delete_user(user):
    db.session.delete(user)
    db.session.commit()
    return user
