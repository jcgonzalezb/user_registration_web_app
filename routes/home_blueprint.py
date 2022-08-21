# flask packages
from flask import Blueprint, render_template

# project resources
from config import app

home_blueprint = Blueprint('home_blueprint', __name__, url_prefix='/')

@home_blueprint.route('/')
def index():
    """
    Home page for this application.
    """
    return render_template('home.html')
