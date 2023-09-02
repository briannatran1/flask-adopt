"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class PetForm(FlaskForm):
    """Form for adding pets."""

    # drop down menu preferred for species and age

    name = StringField('Pet name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(
        ['cat', 'dog', 'porcupine'], message='Species must be cat, dog, or porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = StringField('Age', validators=[InputRequired(), AnyOf(
        ['baby', 'young', 'adult', 'senior'], message='Age must be baby, young, adult, or senior')])
    notes = TextAreaField('Notes', validators=[Optional()])


# add new edit form here
