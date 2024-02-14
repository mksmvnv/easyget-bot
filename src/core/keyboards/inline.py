# Created by @mksmvnv

from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callback_data import Category
from config import sneakers_price, down_jackets_price, other_price


def category_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='👟 Кроссовки', callback_data=Category(category='sneakers', price=sneakers_price))
    keyboard_builder.button(text='🧥 Пуховики', callback_data=Category(category='down_jackets', price=down_jackets_price))
    keyboard_builder.button(text='💻 Другое', callback_data=Category(category='other', price=other_price))
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()
