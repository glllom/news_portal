""" ---------------------NEWS API------------------------------- """
import re

from newsapi import NewsApiClient
from app import user_data

from app.models import User_data




# all data dictionary
data_dict = {'breaking_news_long_string': '', 'articles': []}


def get_news(word=None):
    data_dict['breaking_news_long_string'] = get_headlines()
    if word == '' or word is None:
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=1090ddedde734dbd979190fd2b5f0745"
    else:
        url = f"https://newsapi.org/v2/everything?q={word}&apiKey=1090ddedde734dbd979190fd2b5f0745"

    response = requests.get(url).json()
    if response["totalResults"] <= 0:
        return get_news()
    pattern = r'\[.*\]'
    data_dict['articles'] = []
    for article in response['articles']:
        data_dict['articles'].append({'title': article['title'],
                                      'description': article['description'],
                                      'content': re.sub(pattern, ' ', str(article['content'])),
                                      'urlToImage': article['urlToImage'],
                                      'author': article['author'],
                                      'url': article['url']})
    return data_dict


def get_headlines():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=1090ddedde734dbd979190fd2b5f0745'
    top_headlines = requests.get(url).json()
    headline = ""
    for index, source in enumerate(top_headlines['articles']):
        headline += '\t\tBREAKING NEWS!\t' + source['title']
        if index >= 6:
            break
    return headline

#
#
# """ ------------------------WEATHER API---------------------------- """
# import json
# import requests
# my_key = 'c0779d2b68b69ef6b733d5629c17506f'
# l = 'londo'
# uResponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={l}&appid=c0779d2b68b69ef6b733d5629c17506f")
#
# Jresponse = uResponse.text
# data = json.loads(Jresponse)



""" ------------------------WEATHER API---------------------------- """                                         
import json
import requests
def find_city_id(user_location):
    my_key = 'c0779d2b68b69ef6b733d5629c17506f'
    l = user_location
    uResponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={l}&appid={my_key}")
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    return data['id']

