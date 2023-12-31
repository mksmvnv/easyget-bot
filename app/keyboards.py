from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='💸 Калькулятор')],
        [KeyboardButton(text='💭 О нас')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🏃‍♂️ Назад')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
