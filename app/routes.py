from flask import flash, redirect, render_template, request, url_for
from app import app, db

from app.api import data_dict, find_city_id, get_news
from app.forms import RegistrationForm, LoginForm

from app.models import UserData
from flask_login import LoginManager, login_user, login_required, logout_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return UserData.query.get(int(user_id))


@app.route('/')
@app.route('/<word>')
def index(word=''):
    get_news(word)
    return render_template('index.html', data_dict=data_dict)


@app.route('/specified', methods=['post'])
def specified_news():
    word = request.form.get("search_word")
    return redirect(url_for("index", word=word))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserData.query.filter_by(email=form.email.data).first()
        city = find_city_id(user.location)
        if user:
            if user.password == form.password.data:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('personalized_news', city_id=city))
            else:
                flash('Invalid username or password')
    return render_template('login.html', form=form)


@app.route('/personalized_news/<city_id>')
@login_required
def personalized_news(city_id, word=''):
    get_news(word)
    return render_template('personalized_news.html', data_dict=data_dict, weather=city_id)


@app.route('/signup', methods=['GET', 'POST'])
def signup(word=''):
    get_news(word)
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = UserData(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
                            location=form.location.data, language=form.language.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('New user has been created!')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
