# Created by @mksmvnv

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold, hcode
from aiogram.fsm.context import FSMContext

from core.filters.admin import Admin
from core.keyboards.reply import main_menu_keyboard
from core.keyboards.inline import category_keyboard, back_to_main_menu
from core.utils.db_connect import Request
from core.utils.states import Price
from core.utils.calculator import calculator
from core.utils.currency import current_exchange_rate

from config import admin_id


router = Router()


@router.message(CommandStart())
async def get_start_user(message: Message, request: Request):
    await request.add_user(message.from_user.id, message.from_user.first_name)
    await message.answer(f'👋 Привет, {hbold(message.from_user.first_name)}! Вот и главное меню.',
                         reply_markup=main_menu_keyboard())


@router.message(Command("admin"), Admin(int(admin_id)))
async def get_start_admin(message: Message):
    await message.answer(f'💯 Привет, {hbold(message.from_user.first_name)}! Ты настоящий админ!',
                         reply_markup=main_menu_keyboard())


@router.message(F.text == '🧮 Калькулятор')
async def get_category_keyboard(message: Message, state: FSMContext):
    await state.set_state(Price.logistics)
    await message.answer(f'Выберите категорию товара:',
                         reply_markup=category_keyboard())


@router.message(Price.product)
async def calculation(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(product=message.text)
        data = await state.get_data()
        await state.clear()
        amount = calculator(int(data.get('product')), data.get('logistics'))
        await message.answer(f'Итоговая цена товара: {hcode(str(int(amount)) + '₽')}\n'
                             f'Без учета доставки из Москвы до вашего города.',
                             reply_markup=back_to_main_menu())
    else:
        await message.answer('Некорректное число. Введите еще раз.')


@router.message(F.text == '💰 Актуальный курс')
async def get_category_keyboard(message: Message, state: FSMContext):
    await message.answer(f'Актуальный курс CNY/RUB: {hcode(str(current_exchange_rate - 1) + '₽')}',
                         reply_markup=back_to_main_menu())
