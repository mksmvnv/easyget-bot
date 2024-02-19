# Created by @mksmvnv

from utils.currency import current_exchange_rate

from data.config import china_logistics, fee


def calculator(price, logistics):
    amount = (price + int(china_logistics)) * \
        current_exchange_rate + int(fee) + logistics
    return amount
