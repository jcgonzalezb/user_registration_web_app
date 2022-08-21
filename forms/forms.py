"""
Module for handling the form used new users.
"""
# flask packages
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Email, DataRequired, ValidationError

# project resource
from models.user import User


class RegisterForm(FlaskForm):
    def validate_name(self, name_to_check):
        """
        Function created to validate the name inserted into the form.
        """
        user = User.query.filter_by(name=name_to_check.data).first()
        if user is not None:
            raise ValidationError(
                'El nombre ya existe! Por favor intentar un nombre diferente')

    def validate_email(self, email_to_check):
        """
        Function created to validate the email inserted into the form.
        """
        email = User.query.filter_by(email=email_to_check.data).first()
        if email is not None:
            raise ValidationError(
                'El email ya existe! Por favor intentar un email diferente')

    name = StringField(label='Nombre completo', validators=[
                       Length(min=2, max=80), DataRequired()])
    email = StringField(label='Email', validators=[
                        Length(max=80), Email(), DataRequired()])
    city = StringField(label='Ciudad', validators=[
                       Length(min=2, max=80), DataRequired()])
    submit = SubmitField(label='Crear usuario')
