# Created by @mksmvnv

import os

from dotenv import load_dotenv

load_dotenv()

# Personal data

bot_token = os.getenv('BOT_TOKEN')
admin_id = os.getenv('ADMIN_ID')

# Logistics prices

sneakers_logistics = os.getenv('SNEAKERS_LOGISTICS')
down_jackets_logistics = os.getenv('DOWN_JACKETS_LOGISTICS')
other_logistics = os.getenv('OTHER_LOGISTICS')
china_logistics = os.getenv('CHINA_LOGISTICS')
logistics = os.getenv('LOGISTICS')
fee = os.getenv('FEE')
url = os.getenv('URL')

# Data Base

user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
host = os.getenv('HOST')
port = os.getenv('PORT')
