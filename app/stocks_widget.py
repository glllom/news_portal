"""" ------------------------STOCKS WIDGET---------------------------- """
import requests

key = 'XUWQSSB6CLKKDHX8'

def search_stock():
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=nasdaq&apikey={key}'
    r = requests.get(url)
    data = r.json()
    return data




url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey={key}"
r = requests.get(url)
data = r.json()