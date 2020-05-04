# services/users/project/api/users/models.py


import datetime
import os

import jwt
from flask import current_app
from project import db
from sqlalchemy.sql import func


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    tweets = db.relationship('Tweet', backref='user', lazy=True)

    def __init__(self, username="", email=""):
        self.username = username
        self.email = email

class Tweet(db.Model):

    __tablename__ = "tweets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(140), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class FollowRelationship(db.Model):

    __tablename__ = "follow_relationship"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


if os.getenv("FLASK_ENV") == "development":
    from project import admin
    from project.api.users.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
