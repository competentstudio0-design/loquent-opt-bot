import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router
from google_sheets import init_sheets

load_dotenv()


async def main():
    # 🔥 сначала инициализируем Sheets
    init_sheets()

    # 🤖 создаём bot и dispatcher
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_router(router)

    print("BOT STARTED")

    # 🚀 запускаем polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
