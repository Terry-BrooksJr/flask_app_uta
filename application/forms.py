from curses.ascii import EM
from tkinter import EW
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
<<<<<<< Updated upstream
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('E-Mail/Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

=======
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from application.models import User

class LoginForm(FlaskForm):
    email = StringField('E-Mail/Username', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=8,max=32)])
>>>>>>> Stashed changes
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
<<<<<<< Updated upstream
    email = StringField('E-Mail/Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField(
        'Confirm Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    register = SubmitField('Sign Up')
=======
    email = StringField('E-Mail/Username',validators=[DataRequired(), Email()])
    
    password = StringField('Password', validators=[DataRequired(), Length(min=8, max=32)])
    
    confirm_password = StringField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=32)]);
    
    last_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=32))])
                            

    register = SubmitField('Sign Up')
    
def validate_email(self,email):
    user = User.objects(email=email.data).first()
    if user:
        raise ValidationError("E-Mail already exists! If you have forgotten your password, Please email Password@BrooksJR.com")
>>>>>>> Stashed changes
