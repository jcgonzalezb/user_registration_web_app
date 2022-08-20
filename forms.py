from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    name = StringField(label='Nombre:')
    email = StringField(label='Email:')
    city = StringField(label='Ciudad:')
    submit = SubmitField(label='Crear usuario')
