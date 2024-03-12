# Created by @mksmvnv

import asyncio
import asyncpg
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from handlers import basic, callback
from middlewares.db_middleware import DataBaseSession

from data.config import TOKEN, PGUSER, PGPASS, DB, HOST, PORT


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

    async with asyncpg.create_pool(user=str(PGUSER),
                                   password=str(PGPASS),
                                   database=str(DB),
                                   host=str(HOST),
                                   port=str(PORT),
                                   command_timeout=60) as pool_connect:
        bot = Bot(token=TOKEN, default=DefaultBotProperties(
            parse_mode=ParseMode.HTML))
        dp = Dispatcher()

        dp.include_routers(basic.router, callback.router)
        dp.message.middleware.register(DataBaseSession(pool_connect))

        try:
            await bot.delete_webhook(drop_pending_updates=True)
            await dp.start_polling(bot, timeout=10)
        finally:
            await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
