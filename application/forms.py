from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm):
    email = StringField('E-Mail/Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    email = StringField('E-Mail/Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password',validators=[DataRequired()])
    first_name = StringField('First Name',validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    register = SubmitField('Sign Up')