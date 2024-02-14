# Created by @mksmvnv

from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='⚡ Заказать')
    keyboard_builder.button(text='🧮 Калькулятор')
    keyboard_builder.button(text='💰 Актуальный курс')
    keyboard_builder.button(text='📃 Отзывы')
    keyboard_builder.button(text='📌 О нас')
    keyboard_builder.button(text='🛟 FAQ')
    keyboard_builder.adjust(1, 2, 2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True)
