"""
Module created to hold the class User
"""
# project resource
from config import db


class User(db.Model):
    """
    User Flask-SQLAlchemy Model
    Represents objects contained in the user table
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80), nullable=False)
