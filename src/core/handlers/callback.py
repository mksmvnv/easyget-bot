from aiogram import Bot
from aiogram.types import CallbackQuery


async def get_category_price(call: CallbackQuery):
    result = call.data
    answer = f'Доставка стоит {result}.'
    await call.message.answer(answer)
    await call.answer()
    