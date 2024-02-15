# Created by @mksmvnv

from aiogram.fsm.state import StatesGroup, State


class Price(StatesGroup):
    logistics = State()
    product = State()
