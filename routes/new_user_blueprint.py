# flask packages
from flask import Blueprint, render_template, flash, redirect, url_for

from models.user import User
from forms.forms import RegisterForm
from config import db

new_user_blueprint = Blueprint('new_user_blueprint', __name__, url_prefix='/new_user')

@new_user_blueprint.route('/', methods=['GET', 'POST'], strict_slashes=False)
def new_user():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data,
                              email=form.email.data,
                              city=form.city.data)
        db.session.add(new_user)
        db.session.commit()
        return render_template('added_user.html')
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Hay un error creando un usuario: {err_msg}', category='danger')

    return render_template('new_user.html', form=form)
