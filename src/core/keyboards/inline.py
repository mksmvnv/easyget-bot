# Created by @mksmvnv

from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callback_data import Category, City, Pagination, Link

from data.config import sneakers_logistics, down_jackets_logistics, other_logistics


def category_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='👟 Кроссовки',
                            callback_data=Category(name='sneakers', logistics=sneakers_logistics))
    keyboard_builder.button(text='🧥 Пуховики',
                            callback_data=Category(name='down_jackets', logistics=down_jackets_logistics))
    keyboard_builder.button(text='💻 Другое',
                            callback_data=Category(name='other', logistics=other_logistics))
    keyboard_builder.button(text='↩ Назад в главное меню',
                            callback_data=Pagination(page='main_menu'))
    keyboard_builder.adjust(1, 1, 1, 1)
    return keyboard_builder.as_markup()


def city_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🏢 Москва',
                            callback_data=City(name='moscow'))
    keyboard_builder.button(text='🏛 Санкт-Петербург',
                            callback_data=City(name='spb'))
    keyboard_builder.button(text='🏝 Другой город',
                            callback_data=City(name='other'))
    keyboard_builder.adjust(1, 1, 1)
    return keyboard_builder.as_markup()


def show_reviews():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='🔎 Показать', url='https://vk.com/easyget?w=wall-191811897_126', callback_data=Link(path='reviews'))
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data=Pagination(page='main_menu'))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def show_all_info():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='🔎 Показать', url='https://vk.com/easyget', callback_data=Link(path='faq'))
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data=Pagination(page='main_menu'))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def cancel_order():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='🚫 Отменить заказ', callback_data=Pagination(page='main_menu'))
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def return_to_main_menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='↩ Назад в главное меню', callback_data=Pagination(page='main_menu'))
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
