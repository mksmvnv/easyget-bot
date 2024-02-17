# Created by @mksmvnv

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from core.utils.callback_data import Category, City
from core.utils.states import Calculation, Order
from core.keyboards.inline import cancel_order


router = Router()


@router.callback_query(Category.filter(), Calculation.logistics)
async def select_category_for_calculation(call: CallbackQuery, callback_data: Category, state: FSMContext):
    await state.update_data(logistics=callback_data.logistics)
    await state.set_state(Calculation.product)
    await call.message.answer('Введите цену на товар в юанях:')
    await call.answer()


@router.callback_query(City.filter(), Order.city)
async def select_category_for_order(call: CallbackQuery, callback_data: City, state: FSMContext):
    await state.update_data(name=callback_data.name)
    await state.set_state(Order.link)
    await call.message.answer('Вставьте ссылку на товар из Poizon:', reply_markup=cancel_order())
    await call.answer()


@router.callback_query(F.data == 'main_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.answer()
