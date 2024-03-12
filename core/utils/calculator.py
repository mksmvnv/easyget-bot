# Created by @mksmvnv

from utils.currency import current_exchange_rate

from data.config import CHINA, FEE


def calculator(product, logistics):
    amount = (product + int(CHINA)) * \
        current_exchange_rate + int(FEE) + logistics
    return amount
