# flask packages
from flask import Blueprint, render_template

# project resources
from config import app

index_blueprint = Blueprint('index_blueprint', __name__, url_prefix='/')


@app.route('/')
def index():
    """
    Index page. No token needed
    :return: JSON object
    """
    return render_template('home.html')
