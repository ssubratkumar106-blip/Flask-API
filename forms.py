from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message = "Required your name !, It cannot be empty")])
    email = StringField('Email', validators=[DataRequired(message="Email message is required."), Email(message="Invalid email address.")]) 
    password = PasswordField('Password', validators=[DataRequired(message="Password is required"), Length(min=6, message="Password must be at least 6 characters long")])
    submit = SubmitField('Register')