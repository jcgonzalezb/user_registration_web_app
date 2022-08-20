# project resource
from config import db


class User(db.Model):
    """
    User Flask-SQLAlchemy Model
    Represents objects contained in the users table
    """
    __tablename__ = 'users'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(128), nullable=False)
