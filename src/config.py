# Created by @mksmvnv

import os

from dotenv import load_dotenv

load_dotenv()

# Personal data

bot_token = os.getenv('BOT_TOKEN')
admin_id = os.getenv('ADMIN_ID')

# Logistics prices

sneakers_price = os.getenv('SNEAKERS_PRICE')
down_jackets_price = os.getenv('DOWN_JACKETS_PRICE')
other_price = os.getenv('OTHER_PRICE')

# Data Base

user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
host = os.getenv('HOST')
port = os.getenv('PORT')
