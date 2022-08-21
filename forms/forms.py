from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from models.user import User

class RegisterForm(FlaskForm):
    def validate_name(self, name_to_check):
        name = User.query.filter_by(name=name_to_check.data).first()
        if name:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    name = StringField(label='Nombre')
    email = StringField(label='Email')
    city = StringField(label='Ciudad')
    submit = SubmitField(label='Crear usuario')
