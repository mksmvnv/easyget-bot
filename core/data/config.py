# Created by @mksmvnv

import os

from dotenv import load_dotenv

load_dotenv()

# Personal data

TOKEN = os.environ['TOKEN']
ADMIN_ID = os.getenv('ADMIN_ID')

# Logistics prices

SNEAKERS = os.getenv('SNEAKERS')
JACKETS = os.getenv('JACKETS')
OTHER = os.getenv('OTHER')
CHINA = os.getenv('CHINA')
FEE = os.getenv('FEE')

# Links

CNYURL = os.getenv('CNYURL')
EGURL = os.getenv('EGURL')
REWURL = os.getenv('REWURL')

# Data Base

PGUSER = os.getenv('PGUSER')
PGPASS = os.environ['PGPASS']
DB = os.getenv('DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

# Other

CLASS = os.getenv('CLASS')
