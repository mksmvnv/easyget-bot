import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from config import TOKEN, LOGISTICS, PL, FEE, EXCHANGE_RATE
from app.keyboards import main_menu, back

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f'Привет, {hbold(message.from_user.full_name)} 👋',
                         reply_markup=main_menu)


@dp.message(F.text.in_(['💸 Калькулятор']))
async def question(message: Message):
    await message.reply('Введите цену на товар в юанях:')


@dp.message(lambda x: x.text.isdigit() and int(x.text) > 0)
async def calcutator(message: Message):
    user_input = int(message.text)
    result = (user_input + PL) * \
        EXCHANGE_RATE + (LOGISTICS + FEE)
    await message.reply(
        f'Цена товара в рублях: {
            hbold(int(result))}₽\nБез учета доставки из Мск в Ваш город.',
        reply_markup=back)


@dp.message(F.text.in_(['🏃‍♂️ Назад']))
async def handle_back(message: Message):
    await message.reply(text='Возвращаюсь в главное меню!', reply_markup=main_menu)


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
