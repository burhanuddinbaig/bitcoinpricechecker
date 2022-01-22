import requests

from bs4 import BeautifulSoup as bs

URL = 'https://coinmarketcap.com/currencies/bitcoin/'
r = requests.get(URL)

soup = bs(r.content, 'html.parser')

price = soup.find('div', {'class': 'priceValue'})
extract = price.select_one('span')

print(f'Bitcoin Price Today is {extract.text} per (BTC/USD)')