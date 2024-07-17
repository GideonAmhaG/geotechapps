""" main views module """


from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from .iso import iso
from .forms import InputForm

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """ for home page """
    return render_template('home.html', user=current_user)


@views.route('/about')
def about():
    """ for abouts page """
    return render_template('about.html', user=current_user)


@views.route('/faq')
def faq():
    """ for FAQ page """
    return render_template('faq.html', user=current_user)

@views.route('/privacy-policy')
def privacy_policy():
    """ for privacy-policy page """
    return render_template('privacy_policy.html', user=current_user)

@views.route('/contact-us')
def contact_us():
    """ for contact-us page """
    return render_template('contact_us.html', user=current_user)


@views.route('/found_type', methods=['GET', 'POST'])
def found_type():
    """ allows selection of foundation type """
    if request.method == 'POST':
        option = request.form['option']
        if option == 'iso_square':
            return redirect(url_for('views.soil_type'))
    return render_template('found_type.html', user=current_user)


@views.route('/soil_type', methods=['GET', 'POST'])
def soil_type():
    """
    Handles soil type selection and redirects to foundation design with chosen type.
    """
    if request.method == 'POST':
        option = request.form['option']
        return render_template('inputs.html', user=current_user, soil_type=option)
    return render_template('soil_type.html', user=current_user)


@views.route('/inputs', methods=['POST'])
def inputs():
    """
    Takes inputs and displays results.
    """
    data_vars = [request.form[var] for var in ['DL', 'LL', 'mxp', 'mxv', 'myp',\
                'myv', 'COL', 'COLY', 'FCK', 'FYK', 'BAR', 'COV']]
    com_vars = False
    results, inputs = {}, {}
    if validate_input(data_vars):
        dl, ll, mxp, mxv, myp, myv, col, coly, fck, fyk, bar, cov = map(float, data_vars)
        inputs = {'dl': dl, 'll': ll, 'mxp': mxp, 'mxv': mxv, 'myp': myp, 'myv': myv, 'col': col,
            'coly': coly, 'fck': fck, 'fyk': fyk, 'bar': bar, 'cov': cov}
        com_vars = True
    soil_type = request.form['option']
    bolClay, bolSand, bolBc = False, False, False
    if soil_type == 'clay': # means clay soil
        clay_vars = [request.form[var] for var in ['CU', 'DF', 'GAM']]
        if validate_input(clay_vars):
            cu, df, gam = map(float, clay_vars)
            results = iso(dl, ll, mxp, mxv, myp, myv, col, coly, fck, fyk, bar, cov, soil_type,
                cu=cu, Df=df, gamma=gam)
            inputs.update({'cu': cu, 'df': df, 'gam': gam})
            bolClay = True
    elif soil_type == 'sand': # means sand soil
        sand_vars = [request.form[var] for var in ['PHI', 'DF', 'GAM']]
        if validate_input(sand_vars):
            phi, df, gam = map(float, sand_vars)
            results = iso(dl, ll, mxp, mxv, myp, myv, col, coly, fck, fyk, bar, cov, soil_type,
                phi_f=phi, Df=df, gamma=gam)
            inputs.update({'phi': phi, 'df': df, 'gam': gam})
            bolSand = True
    elif soil_type == 'bearing_c': # means bearing capacity is provided
        bc_vars = [request.form[var] for var in ['BC']]
        if validate_input(bc_vars):
            bc = float(bc_vars[0])
            results = iso(dl, ll, mxp, mxv, myp, myv, col, coly, fck, fyk, bar, cov, soil_type, bc=bc)
            inputs.update({'bc': bc})
            bolBc = True
    if (com_vars and (bolClay or bolSand or bolBc)):
        submit_type = request.form['submit_type']
        user = current_user
        if submit_type == 'regular':
            if not results:
                return render_template('result.html', inputs=inputs, results=results, text="You",
                    submit_type=submit_type, user=current_user)
            else:
                return render_template('result.html', inputs=inputs, results=results, soil_type=soil_type,
                    submit_type=submit_type, user=current_user)
        elif submit_type == 'advanced':
            # if user.is_authenticated:
                if not results:
                    return render_template('result.html', inputs=inputs, results=results, text="You",
                        submit_type=submit_type, user=current_user)
                else:
                    return render_template('result.html', inputs=inputs, results=results, soil_type=soil_type,
                        submit_type=submit_type, user=current_user)
            # else:
            #     return redirect(url_for('auth.login'))
    else:
        return render_template('inputs.html', user=current_user, soil_type=soil_type)


@views.route('/save', methods=['GET', 'POST'])
@login_required
def save():
    """ saves users advanced results """
    if request.method == 'POST':
        note = request.form.get('note')#Gets the note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note
            db.session.add(new_note) #adding the note to the database
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("saved.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    """ deletes the saved advanced results """
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


def is_float(value):
    " checks float "
    try:
        float(value)
        return True
    except ValueError:
        return False


def validate_input(data_vars):
    """
    Validates input data_vars.

    Args:
        data_vars (list): List of input values.

    Returns:
        bool: True if input is valid, False otherwise.
    """
    if any(not var for var in data_vars):
        flash('An input field is blank.', category='error')
        return False
    elif any(not is_float(var) for var in data_vars):
        flash('An input field is not a number.', category='error')
        return False
    return True