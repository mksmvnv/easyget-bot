# Created by @mksmvnv

import requests

from bs4 import BeautifulSoup

from config import url


html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
search_exchange_rate = soup.find(
    'p', {'class': 'result__BigRate-sc-1bsijpp-1 dPdXSB'}).text
current_exchange_rate = float(search_exchange_rate[:5]) + 1
