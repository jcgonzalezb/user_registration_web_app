# flask packages
from flask import Blueprint, render_template

from forms import RegisterForm

new_user_blueprint = Blueprint('new_user_blueprint', __name__, url_prefix='/new_user')

@new_user_blueprint.route('/', strict_slashes=False)
def new_user():
    form = RegisterForm()
    return render_template('new_user.html', form=form)
