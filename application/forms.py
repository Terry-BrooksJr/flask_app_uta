from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from curses.ascii import EM
from tkinter import EW
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from application.models import User

class LoginForm(FlaskForm):
    email = StringField('E-Mail/Username', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=8,max=32)])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('E-Mail/Username',validators=[DataRequired(), Email()])
    
    password = StringField('Password', validators=[DataRequired(), Length(min=8, max=32)])
    
    confirm_password = StringField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=32)]);
    
    last_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=32)])
                            

    register = SubmitField('Sign Up')
    
def validate_email(self,email):
    user = User.objects(email=email.data).first()
    if user:
        raise ValidationError(
            "E-Mail already exists! If you have forgotten your password, Please email Password@BrooksJR.com")


class FieldsRequiredForm(FlaskForm):
  """Require radio fields to have content. This works around the bug that WTForms radio fields don't honor the `DataRequired` or `InputRequired` validators."""
  class Meta:
    def render_field(self, field, render_kw):
      if field.type == "_Option":
        render_kw.setdefault("required", True)
      return super().render_field(field, render_kw)


categories = [("recommended", "Recommended"), ("tovisit",
                                               "Places To Go"), ("visited", "Visited!!!")]

## Create Form Here


class AddLocationForm(FieldsRequiredForm):
  name = StringField("Location Name", validators=[DataRequired])
  description = StringField("Location Description", vaildators=[DataRequired])
  location_cat = RadioField("Location Category", choices=categories, vaildators=[InputRequired])
