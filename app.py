from flask import Flask, render_template, request, redirect, url_for
from newsapi import NewsApiClient
from forms import RegistrationForm
import re

# Init
app = Flask(__name__)
app.secret_key = '13214465469847635431'

newsapi = NewsApiClient(api_key='1090ddedde734dbd979190fd2b5f0745')
# all data dictionary
data_dict = {'breaking_news_long_string':'', 'articles': []}
current_user = {}


def get_news(word):
    top_headlines = newsapi.get_top_headlines(language='en', sources='bbc-news')
    data_dict['breaking_news_long_string'] = '\t\tBREAKING NEWS!\t'.join(
        source['title'] for source in top_headlines['articles'])
    if word == '':
        for article in top_headlines['articles']:
            data_dict['articles'].append({'title': article['title'],
                                          'description': article['description'],
                                          'content': re.sub(r'\[.*\]', '', article['content']),
                                          'urlToImage': article['urlToImage'],
                                          'author': article['author']})


@app.route('/', methods=['GET', 'POST'])
def refresh_all(word=''):
    get_news(word)
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('refresh_all'))
    return render_template('index.html', data_dict=data_dict, form=form, current_user=current_user)


if __name__ == '__main__':
    app.run()
