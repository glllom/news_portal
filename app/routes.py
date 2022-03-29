from flask import flash, redirect, render_template, request, url_for
from app import app

from app.api import data_dict, get_news, find_city_id
from app.forms import RegistrationForm, LoginForm, Update_info
from app.user_data import add_user, check_user, check_password, set_word, get_word, delete_user

logged_user = None


@app.route('/')
@app.route('/<word>')
def index(word=''):
    login_form = LoginForm()
    get_news(word)
    if logged_user:
        try:
            weather_city_id = find_city_id(logged_user.city, logged_user.country)
        except AttributeError:
            weather_city_id = None
    else:
        weather_city_id = None
    return render_template('index.html', data_dict=data_dict, login_form=login_form,
                           logged_user=logged_user, weather_city_id=weather_city_id)


@app.route('/specified', methods=['post'])
def specified_news():
    word = request.form.get("search_word")
    if logged_user:
        set_word(logged_user, word)
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
                return redirect(url_for('index', word=get_word(logged_user)))
            else:
                flash("password incorrect")
        else:
            flash("email incorrect")
    return redirect(url_for('index') + "#login-popup")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        if not check_user(form.email.data):
            add_user(form.firstname.data,
                     form.lastname.data,
                     form.email.data,
                     form.country.data,
                     form.city.data,
                     form.language.data,
                     form.password.data)
            flash("User created successfully.")
            return redirect(url_for('index'))
        else:
            flash("User with this email already exists.")
    return render_template('signup.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if logged_user:
        form = Update_info()
        if form.validate_on_submit():
            delete_user(logged_user.email)
            add_user(form.firstname.data,
                     form.lastname.data,
                     form.email.data,
                     form.country.data,
                     form.city.data,
                     form.language.data,
                     form.password.data)
            flash("User updated successfully.")
            return redirect(url_for('logout'))
    return render_template('dashboard.html', form=form, user=logged_user)


@app.route('/logout')
def logout():
    global logged_user
    logged_user = None
    return redirect(url_for('index'))
