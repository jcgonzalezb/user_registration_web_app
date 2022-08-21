"""
Module created to configure the web application
"""
# flask packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create flask app
app = Flask(__name__)

# Connection to the database
db_file = 'users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '6dee850c-8bf4-4f1f-8dc5-729beb79eb1c'

# Create a database object using the SQLAlchemy class,
# passing the application instance to connect the Flask
# application with SQLAlchemy.
db = SQLAlchemy(app)
