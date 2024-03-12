# Created by @mksmvnv

import re

from random import getrandbits

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold, hcode, hitalic
from aiogram.fsm.context import FSMContext

from filters.admin import Admin
from keyboards import inline
from keyboards.reply import main_menu_keyboard
from utils.db_connect import Request
from utils.states import Calculation, Order
from utils.calculator import calculator
from utils.currency import current_exchange_rate

from data.config import ADMIN_ID


router = Router()


@router.message(CommandStart())
async def start_user_message(message: Message, request: Request):
    await request.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name)
    await message.answer(f'👋 Привет, {hbold(message.from_user.first_name)}! Вот и главное меню.',
                         reply_markup=main_menu_keyboard())


@router.message(Command("admin"), Admin(int(ADMIN_ID)))
async def start_admin_message(message: Message):
    await message.answer(f'💯 Привет, {hbold(message.from_user.first_name)}! Ты настоящий админ!',
                         reply_markup=main_menu_keyboard())


@router.message(F.text == '⚡ Заказать')
async def category_order_message(message: Message, state: FSMContext):
    await state.set_state(Order.city)
    await message.answer(f'Выберите город доставки:',
                         reply_markup=inline.city_keyboard())


@router.message(F.text == '🧮 Калькулятор')
async def category_calculator_message(message: Message, state: FSMContext):
    await state.set_state(Calculation.logistics)
    await message.answer(f'Выберите категорию товара:',
                         reply_markup=inline.category_keyboard())


@router.message(F.text == '💰 Актуальный курс')
async def current_exchange_rate_message(message: Message):
    await message.answer(f'Актуальный курс CNY/RUB: {hcode(str(current_exchange_rate - 1) + "₽")}',
                         reply_markup=inline.return_to_main_menu())


@router.message(F.text == '📃 Отзывы')
async def category_order_message(message: Message):
    await message.answer(f'Все отзывы по ссылке ниже.',
                         reply_markup=inline.show_reviews())


@router.message(F.text == '📌 О нас')
async def category_order_message(message: Message):
    await message.answer('Кто мы?\n\n'
                         'easyget. — это сервис доставки оригинальных товаров с площадки Poizon. '
                         'Наша цель — помочь людям из РФ купить любой бренд, любую модель одежды и обуви, техники, '
                         'которую они захотят, в эти непростые времена ограничений, '
                         'когда во всех магазинах нашей необъятной страны пусто и безвкусно. '
                         'Товар полностью оригинальный, проходит проверку Legit-Check. '
                         'Цены ниже рыночных, благодаря воздействию внутреннего китайского рынка.',
                         reply_markup=inline.return_to_main_menu())


@router.message(F.text == '🛟 FAQ')
async def category_order_message(message: Message):
    await message.answer(f'Все инструкции и подробнее о нашей компании вы можете посмотреть в официальной группе по ссылке ниже.',
                         reply_markup=inline.show_all_info())


@router.message(Calculation.price)
async def calculation_message(message: Message, state: FSMContext):
    try:
        price = int(message.text)
        calc_data = await state.get_data()
        amount = calculator(price,
                            calc_data.get('logistics'))
        await message.answer(f'Итоговая цена товара: {hcode(str(int(amount)) + "₽")}\n',
                             reply_markup=inline.return_to_main_menu())
        await state.clear()
    except (TypeError, ValueError):
        await message.answer('🥺 Некорректное число. Введите еще раз.')


@router.message(Order.link)
async def order_message(message: Message, bot: Bot, state: FSMContext):
    pattern = r"https://dw4\.co/t/A/[^ ]+"
    search = re.search(pattern, message.text)
    if search:
        link = search.group(0)
        await state.update_data(link=link)
        order_data = await state.get_data()
        order_number = getrandbits(32)
        await message.answer(f'✅ {hbold(message.from_user.first_name)}, ваш заказ успешно оформлен!\n\n'
                             f'Заказ №: {hcode(order_number)}\n'
                             f'Город: {hcode(order_data.get("name"))}\n'
                             f'Логин: {hcode(message.from_user.username)}\n'
                             f'Ссылка на товар: {order_data.get("link")}\n\n'
                             f'{hitalic("💬 Ожидайте сообщения от нашего менеджера.")}', reply_markup=inline.return_to_main_menu())
        order_info = f'Заказ №: {hcode(order_number)}\n'\
            f'Имя: {hcode(message.from_user.first_name)}\n'\
            f'Логин: {hcode(message.from_user.username)}\n'\
            f'Город: {hcode(order_data.get("name"))}\n'\
            f'Ссылка на товар: {order_data.get("link")}'
        await bot.send_message(ADMIN_ID, order_info)
        await state.clear()
    else:
        await message.answer('🥺 Некорректная ссылка. Введите еще раз.')
