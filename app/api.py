""" ---------------------NEWS API------------------------------- """
import re
import json
import requests
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='cb21ebc4040344cfa657a8490189aa29')
# all data dictionary
data_dict = {'breaking_news_long_string': '', 'articles': []}


def get_news(word=None):
    data_dict['breaking_news_long_string'] = get_headlines()

    if word == '' or word is None:
        response = newsapi.get_top_headlines(language='en', sources='bbc-news')
    else:
        response = newsapi.get_everything(q=word, sources='bbc-news,the-verge',
                                          language='en',
                                          sort_by='relevancy',
                                          page=1)
    if response["totalResults"] <= 0:
        return get_news()
    pattern = r'\[.*\]'
    data_dict['articles'] = []
    for index, article in enumerate(response['articles']):
        data_dict['articles'].append({'title': article['title'],
                                      'description': article['description'],
                                      'content': re.sub(pattern, ' ', str(article['content'])),
                                      'urlToImage': article['urlToImage'],
                                      'author': article['author'],
                                      'url': article['url']})
        if index >= 10:
            break
    return data_dict


def get_headlines():
    top_headlines = newsapi.get_top_headlines(language='en', sources='bbc-news')
    headline = ""
    for index, source in enumerate(top_headlines['articles']):
        headline += '\t\tBREAKING NEWS!\t' + source['title']
        if index >= 6:
            break
    return headline


"""" ------------------------WEATHER API---------------------------- """


def find_country_code(user_country):
    response = requests.get(f"https://restcountries.com/v3.1/name/{user_country}")
    if response.status_code == 404:
        print("unknown country")
        return "IL"
    try:
        return response.json()[0]['cca2']
    except KeyError:
        return "IL"


def find_city_id(city, user_country):
    my_key = 'c0779d2b68b69ef6b733d5629c17506f'
    country = find_country_code(user_country)
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={my_key}")
    if response.status_code == 404:
        return 281184  # Jerusalem
    try:
        return response.json()['id']
    except KeyError:
        print("unknown city")
        return 281184  # Jerusalem

# print(find_city_id("Bat yam", "israel"))
