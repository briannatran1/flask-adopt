"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Pet name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message='Species must be cat, dog, or porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = StringField('Age', validators=[InputRequired(), AnyOf(['baby', 'young', 'adult', 'senior'], message='Age must be baby, young, adult, or senior')])
    notes = TextAreaField('Notes', validators=[Optional()])

                      #choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])