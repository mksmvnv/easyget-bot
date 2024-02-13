from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import SHIP, DJ


def category_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Шип', callback_data=str(SHIP))
    keyboard_builder.button(text='Пуховики', callback_data=str(DJ))
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()
    