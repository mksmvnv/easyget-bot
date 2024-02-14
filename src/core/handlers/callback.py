# Created by @mksmvnv

from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callback_data import Category


async def select_category(call: CallbackQuery, callback_data: Category):
    category = callback_data.category
    price = callback_data.price
    answer = f'{category} - Хороший выбор! Стоимость логистики по данной категории - {price}'
    await call.message.answer(answer)
    await call.answer()
