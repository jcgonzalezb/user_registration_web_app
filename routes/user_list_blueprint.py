"""
Module for the creation of a list of users created.
The users are saved in the database.
"""
# flask packages
from flask import Blueprint, render_template

# project resource
from models.user import User

user_list_blueprint = Blueprint(
    'user_list_blueprint', __name__, url_prefix='/user_list')


@user_list_blueprint.route('/',  methods=['GET'], strict_slashes=False)
def list():
    """
    Function to list all the users created.
    """
    users = User.query.all()
    return render_template("user_list.html", users=users)
