# Created by @mksmvnv

from aiogram.fsm.state import StatesGroup, State


class Calculation(StatesGroup):
    logistics = State()
    price = State()


class Order(StatesGroup):
    city = State()
    link = State()
