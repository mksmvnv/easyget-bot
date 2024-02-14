# Created by @mksmvnv

import asyncio
import asyncpg
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from config import bot_token, user, password, database, host, port
from core.handlers.basic import get_start, get_category_keyboard
from core.handlers.callback import select_category
from core.utils.callback_data import Category
from core.middlewares.db_middleware import DbSession


async def create_pool():
    return await asyncpg.create_pool(user=user, password=password, database=database,
                                     host=host, port=port, command_timeout=60)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    
    bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
    
    pool_connect = await create_pool()

    dp = Dispatcher()
    dp.message.middleware.register(DbSession(pool_connect))
    dp.message.register(get_start, CommandStart())
    dp.message.register(get_category_keyboard)
    dp.callback_query.register(select_category, Category.filter())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
