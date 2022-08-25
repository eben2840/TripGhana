
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Name')
    password = StringField('Phone', validators=[DataRequired()], description='Yes', render_kw={"placeholder": "Phone"})
    email =  StringField('email', validators=[DataRequired()], render_kw={"placeholder": "Email"})
    department = SelectField('Department', choices=[('IT','IT')])
    identification = StringField('identification',  validators=[DataRequired()], render_kw={"placeholder": "Identification"})
    submit = SubmitField('Sign Up')