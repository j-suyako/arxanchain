from flask_login import UserMixin
from . import db, login_manager


class User(UserMixin, db.Model):
    pass


class Person(User):
    __tablename__ = "Person"
    id = db.Column(db.Integer)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))


class Organization(User):
    __tablename__ = "Organization"
    id = db.Column(db.Integer)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
