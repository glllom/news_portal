import json
from flask import flash, redirect, render_template, request, url_for
from app import app
from app.api import data_dict, get_news, find_city_id
from app.forms import RegistrationForm, LoginForm, UpdateInfo
from app.models import User_Stocks
from app.stocks_widget import currency_details, stock_details
from app.user_data import add_stock, add_user, check_user, check_password, remove_stock, set_word, get_word, update_user, user_stocks

logged_user = None

@app.route('/')
@app.route('/search<word>')
def index(word=''):
    login_form = LoginForm()
    get_news(word)
    
    if logged_user:
        try:
            weather_city_id = find_city_id(logged_user.__dict__['city'], logged_user.__dict__['country'])
            print(logged_user.__dict__['city'])
        except AttributeError:
            print("error")
            weather_city_id = None
    else:
        weather_city_id = None
    return render_template('index.html', data_dict=data_dict, login_form=login_form,
                           logged_user=logged_user, weather_city_id=weather_city_id)


@app.route('/stocks')
@app.route('/stocks/<stock>')
def stocks():
    if logged_user:
        personal_stocks = user_stocks(logged_user.id)
        with open('all_stocks_list.json', 'r') as f:
                stocks_list = json.load(f)
        return render_template("stocks.html", stocks=stocks_list, user_stocks=personal_stocks)
    else:
        return redirect(url_for('index'))
    

@app.route('/stock_search', methods=['post'])
def stock_search():
        stock = request.form.get("search_stock")
        stock_symbol = stock.split(':')[0]
        stock_name = stock.split(':')[-1]
        stock = stock_details(stock_symbol)
        add_stock(stock_symbol, stock_name, stock['opening'], stock['high'], stock['low'], stock['previous_close'], stock['closing'], stock['change'], stock['perc'], logged_user.id)

        return redirect(url_for("stocks"))

@app.route('/stocks/<int:stock_id>')
def permanently_remove(stock_id):
        delete_stock = User_Stocks.query.filter_by(id=stock_id).first()
        remove_stock(delete_stock)
        return redirect(url_for('stocks'))

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
    form = UpdateInfo()
    if logged_user:
        if form.validate_on_submit():
            update_user(logged_user, form.firstname.data,
                        form.lastname.data, form.country.data,
                        form.city.data, form.language.data)
            flash("User updated successfully.")
            return redirect(url_for('index'))
        return render_template('dashboard.html', form=form, user=logged_user)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    global logged_user
    logged_user = None
    return redirect(url_for('index'))


@app.route('/test')
def test():
    djd = stock_details('DJD')
    dax = stock_details('DAX')
    eur_ils = currency_details('EUR', 'ILS')
    usd_ils = currency_details('USD', 'ILS')
    return render_template('stocks_widget.html', djd=djd, dax=dax, eur_ils=eur_ils, usd_ils=usd_ils)