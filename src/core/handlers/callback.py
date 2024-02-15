# Created by @mksmvnv

from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from core.keyboards.reply import main_menu_keyboard
from core.utils.callback_data import Category
from core.utils.states import Price


router = Router()


@router.callback_query(Category.filter(), Price.logistics)
async def select_category(call: CallbackQuery, callback_data: Category, state: FSMContext):
    await state.update_data(logistics=callback_data.logistics)
    await state.set_state(Price.product)
    await call.message.answer('Введите цену на товар в юанях:')
    await call.answer()


@router.callback_query(F.data == 'main_menu')
async def back_to_main_menu(call: CallbackQuery):
    await call.answer()
