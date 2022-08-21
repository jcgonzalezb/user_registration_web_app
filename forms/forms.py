from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from models.user import User

class RegisterForm(FlaskForm):
    def validate_name(self, name_to_check):
        name = User.query.filter_by(name=name_to_check.data).first()
        print(name)
        if name:
            raise ValidationError('Name already exists! Please try a different username')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    name = StringField(label='Nombre', validators=[Length(min=2, max=80), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    city = StringField(label='Ciudad', validators=[Length(min=2, max=80), DataRequired()])
    submit = SubmitField(label='Crear usuario')
