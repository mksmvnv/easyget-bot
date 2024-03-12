# Created by @mksmvnv

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from utils.callback_data import Category, City, Pagination
from utils.states import Calculation, Order
from keyboards.inline import cancel_order
from keyboards.reply import main_menu_keyboard


router = Router()


@router.callback_query(City.filter(), Order.city)
async def select_category_for_order(call: CallbackQuery, callback_data: City, state: FSMContext):
    await state.update_data(name=callback_data.name)
    await state.set_state(Order.link)
    await call.message.answer(f'Вставьте ссылку на товар из Poizon:', reply_markup=cancel_order())
    await call.answer()


@router.callback_query(Category.filter(), Calculation.logistics)
async def select_category_for_calculation(call: CallbackQuery, callback_data: Category, state: FSMContext):
    await state.update_data(logistics=callback_data.logistics)
    await state.set_state(Calculation.price)
    await call.message.answer('Введите цену на товар в юанях:')
    await call.answer()


@router.callback_query(Pagination.filter())
async def select_return_to_main_menu(call: CallbackQuery):
    await call.message.answer(f'{hbold(call.from_user.first_name)}, возвращаемся в главное меню!',
                              reply_markup=main_menu_keyboard())
    await call.answer()
