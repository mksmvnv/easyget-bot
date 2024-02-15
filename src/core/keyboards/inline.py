# Created by @mksmvnv

from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.utils.callback_data import Category

from config import sneakers_logistics, down_jackets_logistics, other_logistics


def category_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='👟 Кроссовки',
                            callback_data=Category(name='sneakers', logistics=sneakers_logistics))
    keyboard_builder.button(text='🧥 Пуховики',
                            callback_data=Category(name='down_jackets', logistics=down_jackets_logistics))
    keyboard_builder.button(text='💻 Другое',
                            callback_data=Category(name='other', logistics=other_logistics))
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()


def back_to_main_menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data='main_menu')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
