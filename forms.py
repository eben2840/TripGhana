
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    comment =  StringField('comment', validators=[DataRequired()])
    budget = SelectField('budget',  validators=[DataRequired()], choices=[('Pick a budget-Ghc','Pick a budget-Ghc'),('Ghc20-GHc50', 'GHc20-Ghc50'), ('Ghc50-Ghc100','Ghc50-Ghc100'), ('Ghc500-Ghc1000','Ghc500-Ghc1000'), ('Ghc2000 ', 'Ghc2000 '), ('Ghc3000','Ghc3000') ], default=None )
    submit = SubmitField('submit')  
 
class First(FlaskForm):
    name =  StringField('name', validators=[DataRequired()])
    submit = SubmitField('submit')  
 
 
 
class Add(FlaskForm):
    phone =  StringField('phone', validators=[DataRequired()])
    submit = SubmitField('submit')  
   # budget =SelectField('budget', validate_choice=[('Gh<span>&#8373;</span>:10,Gh<span>&#8373;</span>:100')('Gh<span>&#8373;</span>:100,,Gh<span>&#8373;</span>:500,')])
    