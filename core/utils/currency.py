# Created by @mksmvnv

import requests

from bs4 import BeautifulSoup

from data.config import CNYURL, CLASS


html = requests.get(CNYURL)
soup = BeautifulSoup(html.text, 'lxml')
search_exchange_rate = soup.find(
    'p', {'class': CLASS}).text
current_exchange_rate = float(search_exchange_rate[:5]) + 1
