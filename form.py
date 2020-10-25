from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator

##creating a class for password

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()] )
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#new class for forget password

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()] )
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember about me')
    submit = SubmitField('Login')