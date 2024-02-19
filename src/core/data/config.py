# Created by @mksmvnv

import os

from dotenv import load_dotenv

load_dotenv()

# Personal data

bot_token = str(os.getenv('BOT_TOKEN'))
admin_id = os.getenv('ADMIN_ID')

# Logistics prices

sneakers_logistics = os.getenv('SNEAKERS_LOGISTICS')
down_jackets_logistics = os.getenv('DOWN_JACKETS_LOGISTICS')
other_logistics = os.getenv('OTHER_LOGISTICS')
china_logistics = os.getenv('CHINA_LOGISTICS')
fee = os.getenv('FEE')
url = str(os.getenv('URL'))

# Data Base

pguser = str(os.getenv('PGUSER'))
pgpassword = str(os.getenv('PGPASSWORD'))
database = str(os.getenv('DATABASE'))
host = str(os.getenv('HOST'))
port = os.getenv('PORT')
