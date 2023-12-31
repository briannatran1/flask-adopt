"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/', methods=['GET'])
def show_pet_listing():
    """Shows list of pets"""
    pets = Pet.query.all()

    return render_template('homepage.html',
                           pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """Shows adding a new pet form"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
        )

        db.session.add(pet)
        db.session.commit()

        flash(f'Added {name}')
        return redirect('/')

    else:
        return render_template('pet_add_form.html',
                               form=form)


# combine show_pet_details with edit_pet
# use syntax for default image

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_details(pet_id):
    """Shows pet details on a specific pet"""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_details_page.html', pet=pet)


@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Show pet edit form and handle edit"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        # pet.available = form.available.data

        db.session.commit()
        flash(f'Pet {pet_id} updated!')
        return redirect(f'/{pet_id}')

    else:
        return render_template('edit_pet_form.html',
                               form=form)
