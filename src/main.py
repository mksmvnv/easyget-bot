from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from core.handlers.basic import get_start

import os
import asyncio
import logging

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text='Бот остановлен!')
   

async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(token=TOKEN, parse_mode='HTML')
    
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
