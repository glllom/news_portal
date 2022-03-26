""" ---------------------NEWS API------------------------------- """
import re
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='cb21ebc4040344cfa657a8490189aa29')
# all data dictionary
data_dict = {'breaking_news_long_string':'', 'articles': []}


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
                                          'author': article['author'],
                                          'url': article['url']})


""" ------------------------WEATHER API---------------------------- """                                         
import json
import requests
my_key = 'c0779d2b68b69ef6b733d5629c17506f'
l = 'londo'
uResponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={l}&appid=c0779d2b68b69ef6b733d5629c17506f")

Jresponse = uResponse.text
data = json.loads(Jresponse)