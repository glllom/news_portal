from flask import flash, redirect, render_template, request, url_for
from app import app, db
from app.api import data_dict, get_news
from app.forms import RegistrationForm
from app.models import User_data


@app.route('/', methods=['GET', 'POST'])
def refresh_all(word=''):
    get_news(word)
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('refresh_all'))
    return render_template('index.html', data_dict=data_dict, form=form, current_user=current_user)