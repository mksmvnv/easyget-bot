from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from core.handlers.basic import get_start, get_hello
from core.utils.commands import set_commands

import os
import asyncio
import logging


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(ADMIN_ID, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text='Бот остановлен!')
   

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')


    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, CommandStart())
    dp.message.register(get_hello, F.text == 'Привет!')
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
