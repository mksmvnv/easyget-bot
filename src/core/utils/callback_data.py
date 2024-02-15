# Created by @mksmvnv

from aiogram.filters.callback_data import CallbackData


class Category(CallbackData, prefix='category'):
    name: str
    logistics: int
