from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from core.keyboards.reply import main_menu_keyboard
from core.keyboards.inline import category_keyboard


async def get_start(message: Message):
    await message.answer(f'Привет, {hbold(message.from_user.first_name)}!',
                         reply_markup=main_menu_keyboard())


async def get_hello(message: Message):
    await message.reply(f'И тебе привет! Давай расчитаем стоимость твоего заказа?')
    

async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Выберите категорию товара:',
                         reply_markup=category_keyboard())
    