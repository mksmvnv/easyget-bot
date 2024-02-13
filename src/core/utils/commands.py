from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
       commands = [
           BotCommand(
               command='start',
               description='Начало работы'
           ),
           BotCommand(
               command='menu',
               description='Главное меню'
           ),
           BotCommand(
              command='category',
              description='Категории'
           ),
           BotCommand(
               command='help',
               description='Поддержка'
           ),
           BotCommand(
               command='cencel',
               description='Назад'
           )
           
       ]
       
       await bot.set_my_commands(commands, BotCommandScopeDefault())
    