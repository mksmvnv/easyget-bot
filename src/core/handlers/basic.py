from aiogram.types import Message
from aiogram.utils.markdown import hbold
from core.keyboards.reply import main_menu


async def get_start(message: Message):
    await message.answer(f'Привет, {hbold(message.from_user.first_name)}!',
                         reply_markup=main_menu())


async def get_hello(message: Message):
    await message.reply(f'И тебе привет! Давай расчитаем стоимость твоего заказа?')