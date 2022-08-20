# SQLAlchemy package
# from sqlalchemy.dialects.mysql import INTEGER

# project resource
from config import db


class User(db.Model):
    """
    User Flask-SQLAlchemy Model
    Represents objects contained in the users table
    """
    __tablename__ = 'users'

    id = db.Column(INTEGER(unsigned=True), primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, nullable=False)
    city = db.Column(db.String(128), nullable=False)
