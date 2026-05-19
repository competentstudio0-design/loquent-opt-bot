import asyncio
from aiogram import Bot, Dispatcher
from app.bot.handlers import router
from app.bot.config import BOT_TOKEN
from app.core.sheets import init_sheets

async def main():
    init_sheets()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    print('BOT STARTED')
    await dp.start_polling(bot)
