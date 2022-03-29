from flask import flash, redirect, render_template, request, url_for, g
from app import app

from app.api import data_dict, find_city_id, get_news
from app.forms import RegistrationForm, LoginForm

from app.user_data import add_user, check_user, check_password
logged_user = None


@app.route('/')
@app.route('/<word>')
def index(word=''):
    login_form = LoginForm()
    get_news(word)
    return render_template('index.html', data_dict=data_dict, login_form=login_form, logged_user=logged_user)


@app.route('/specified', methods=['post'])
def specified_news():
    word = request.form.get("search_word")
    return redirect(url_for("index", word=word))


@app.route('/login', methods=['POST'])
def login():
    global logged_user
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if user := check_user(email):
            if check_password(email, password):
                logged_user = user
                return redirect(url_for('index'))
            else:
                flash("password incorrect")
        else:
            flash("email incorrect")
    return redirect(url_for('index')+"#login-popup")


@app.route('/personalized_news/<city_id>')
# @login_required
def personalized_news(city_id, word=''):
    get_news(word)
    return render_template('personalized_news.html', data_dict=data_dict, weather=city_id)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        if not check_user(form.email.data):
            add_user(form.firstname.data,
                     form.lastname.data,
                     form.email.data,
                     form.location.data,
                     form.language.data,
                     form.password.data)
            flash("User created successfully.")
            return redirect(url_for('index'))
        else:
            flash("User with this email already exists.")
    return render_template('signup.html', form=form, data_dict=data_dict)


@app.route('/logout')
def logout():
    global logged_user
    logged_user = None
    return redirect(url_for('index'))
