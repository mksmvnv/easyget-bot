# Created by @mksmvnv

from core.utils.currency import current_exchange_rate

from config import china_logistics, fee


def calculator(price, logistics):
    amount = (price + int(china_logistics)) * \
        current_exchange_rate + int(fee) + logistics
    return amount
