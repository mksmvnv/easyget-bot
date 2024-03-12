# Created by @mksmvnv

from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callback_data import Category, City, Pagination, Link

from data.config import SNEAKERS, JACKETS, OTHER, EGURL, REWURL


def category_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='👟 Кроссовки',
                            callback_data=Category(name='Кроссовки', logistics=SNEAKERS))
    keyboard_builder.button(text='🧥 Пуховики',
                            callback_data=Category(name='Пуховики', logistics=JACKETS))
    keyboard_builder.button(text='💻 Другое',
                            callback_data=Category(name='Другое', logistics=OTHER))
    keyboard_builder.button(text='↩ Назад в главное меню',
                            callback_data=Pagination(page='Главное меню'))
    keyboard_builder.adjust(1, 1, 1, 1)
    return keyboard_builder.as_markup()


def city_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🏢 Москва',
                            callback_data=City(name='Москва'))
    keyboard_builder.button(text='🏛 Санкт-Петербург',
                            callback_data=City(name='Санкт-Петербург'))
    keyboard_builder.button(text='🏝 Другой город',
                            callback_data=City(name='Другой'))
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()


def show_reviews():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='🔎 Показать', url=REWURL, callback_data=Link(path='Отзывы'))
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data=Pagination(page='Главное меню'))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def show_all_info():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='🔎 Показать', url=EGURL, callback_data=Link(path='FAQ'))
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data=Pagination(page='Главное меню'))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def cancel_order():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='🚫 Отменить заказ', callback_data=Pagination(page='Главное меню'))
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def return_to_main_menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data=Pagination(page='Главное меню'))
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
