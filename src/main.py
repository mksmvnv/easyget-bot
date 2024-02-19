# Created by @mksmvnv

import asyncio
import asyncpg
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from core.handlers import basic, callback
from core.middlewares.db_middleware import DbSession

from config import bot_token, user, password, database, host, port


async def create_pool():
    return await asyncpg.create_pool(user=user,
                                     password=password,
                                     database=database,
                                     host=host,
                                     port=port,
                                     command_timeout=60)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

    bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
    pool_connect = await create_pool()
    dp = Dispatcher()

    dp.include_routers(basic.router, callback.router)
    dp.message.middleware.register(DbSession(pool_connect))

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
