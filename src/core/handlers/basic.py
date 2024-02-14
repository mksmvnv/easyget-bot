# Created by @mksmvnv

from aiogram.types import Message
from aiogram.utils.markdown import hbold
from core.keyboards.reply import main_menu_keyboard
from core.keyboards.inline import category_keyboard
from core.utils.db_connect import Request


async def get_start(message: Message, request: Request):
    await request.add_user(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Привет, {hbold(message.from_user.first_name)}!',
                         reply_markup=main_menu_keyboard())


async def get_category_keyboard(message: Message):
    await message.answer(f'Выберите категорию товара:',
                         reply_markup=category_keyboard())
