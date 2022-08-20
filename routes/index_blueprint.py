# flask packages
from flask import Blueprint, jsonify, render_template

# project resources
from config import app, db
from models.user import User

index_blueprint = Blueprint('index_blueprint', __name__, url_prefix='/')


@app.route('/')
def index():
    """
    Index page. No token needed
    :return: JSON object
    """
    return render_template('welcome.html')
