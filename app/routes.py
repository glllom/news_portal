from flask import flash, redirect, render_template, request, url_for
from app import app, db
from app.api import get_news
from app.forms import RegistrationForm
from app.models import User_data


@app.route('/', methods=['GET', 'POST'])
def refresh_all():
    word = request.form.get("search_word") if request.method == "POST" else ""
    data_dict = get_news(word)
    form = RegistrationForm()
    return render_template('index.html', data_dict=data_dict, form=form)

#
# @app.route('/specify/', methods=['GET', 'POST'])
# def specify():
#     data_dict = get_news(request.form.get("search_word"))
#     print("data_dict, clinton=", data_dict["articles"][0])
#     form = RegistrationForm()
#     return render_template('index.html', data_dict=data_dict, form=form)
