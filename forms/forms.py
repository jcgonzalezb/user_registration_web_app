from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Email, DataRequired, ValidationError
from models.user import User

class RegisterForm(FlaskForm):
    def validate_name(self, name_to_check):
        user = User.query.filter_by(name=name_to_check.data).first()
        if user is not None:
            raise ValidationError('El nombre ya existe! Por favor intentar un nombre diferente')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email is not None:
            raise ValidationError('El email ya existe! Por favor intentar un email diferente')

    name = StringField(label='Nombre', validators=[Length(min=2, max=80), DataRequired()])
    email = StringField(label='Email', validators=[Length(max=80), Email(), DataRequired()])
    city = StringField(label='Ciudad', validators=[Length(min=2, max=80), DataRequired()])
    submit = SubmitField(label='Crear usuario')
