# Created by @mksmvnv

from aiogram.filters.callback_data import CallbackData


class Category(CallbackData, prefix='category'):
    name: str
    logistics: int


class City(CallbackData, prefix='city'):
    name: str


class Pagination(CallbackData, prefix='pag'):
    page: str


class Link(CallbackData, prefix='link'):
    path: str
