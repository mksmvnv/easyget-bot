# Created by @mksmvnv

import os

# Personal data

BOT_TOKEN = os.environ['TOKEN']
ADMIN_ID = 714689915

# Logistics prices

SNEAKERS_LOGISTICS = 1500
DOWN_JACKETS_LOGISTICS = 850
OTHER_LOGISTICS = 1500
CHINA_LOGISTICS = 50
FEE = 1000
URL = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=RUB'

# Data Base

PGUSER = 'easyget'
PGPASSWORD = os.environ['PASS']
DATABASE = 'db_easyget'
HOST = 'localhost'
PORT = 5432
