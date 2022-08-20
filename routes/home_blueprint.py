# flask packages
from flask import Blueprint, render_template

# project resources
from config import app

home_blueprint = Blueprint('home_blueprint', __name__, url_prefix='/')

@home_blueprint.route('/')
def index():
    """
    Home page. No token needed
    :return: JSON object
    """
    return render_template('home.html')
