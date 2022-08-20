# project resource
from config import db


class User(db.Model):
    """
    User Flask-SQLAlchemy Model
    Represents objects contained in the users table
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(80), nullable=False)
