from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField


class FactorialForm(FlaskForm):
    num1 = IntegerField('Enter a number?')
    submit = SubmitField('Factorial!')