"""" ------------------------STOCKS WIDGET---------------------------- """
import csv
import json
import requests

""" ------------API KEY------------ """

key = 'XUWQSSB6CLKKDHX8'
stock_info = {}

def exchange_rates(currency_from, currency_to):
    response = requests.get(f'https://api.frankfurter.app/latest?amount=1&from={currency_from}&to={currency_to}')
    if response.status_code == 404:
        return 'Information not available in this moment, try again later or choose a different stock.'
    try:
        return response.json()
    except KeyError:
        return 'No info'

def currency_details(currency_from, currency_to):
    currency = exchange_rates(currency_from, currency_to)
    from_currency = (f'{currency_from}').upper()
    to_currency = (f'{currency_to}').upper()
    exchange_rate = currency['rates'][f'{currency_to}']
    return {'from_currency':from_currency, 'to_currency':to_currency, 'exchange_rate':exchange_rate}


def search_stock(stock_symbol):
    response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={key}')
    if response.status_code == 404:
        return 'Information not available in this moment, try again later or choose a different stock.'
    try:
        return response.json()
    except KeyError:
        return 'No info'

def stock_details(stock_symbol):
    stock = search_stock(stock_symbol)
    try:
        date = stock['Global Quote']['07. latest trading day']
        opening = stock['Global Quote']['02. open']
        high = stock['Global Quote']['03. high']
        low = stock['Global Quote']['04. low']
        previous_close = stock['Global Quote']['08. previous close']
        closing = stock['Global Quote']['05. price']
        change = stock['Global Quote']['09. change']
        perc = stock['Global Quote']['10. change percent']
        return {'date': date, 'opening':opening, 'high': high, 'low': low, 'previous_close':previous_close, 'closing':closing, 'change':change, 'perc':perc }
    except KeyError:
        return {'date': 'api timeout', 'opening':5.0, 'high': 5.0, 'low': 5.0, 'previous_close':5.0, 'closing':5.0, 'change':5.0, 'perc':'api timeout' }

""" -----------------OPTIONAL A LIST OF ONLY LATEST TRADES STOCKS --------------------"""
""" def load_trading_stocks():
    with requests.Session() as s:
        download = s.get('https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=XUWQSSB6CLKKDHX8')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        dict_keys = ['symbol', 'name']
        list_of_todays_stocks = [dict(zip(dict_keys, i)) for i in my_list[1:] ]
        with open ('today_trading_stocks.json', 'w') as f:
            f.truncate(0)
            f.seek(0)       
            json.dump(list_of_todays_stocks, f) """