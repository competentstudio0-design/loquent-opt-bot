import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router
from google_sheets import init_sheets

load_dotenv()


async def main():
    # 🔥 важно: сначала всё внешнее
    init_sheets()

    token = os.getenv("BOT_TOKEN")

    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(router)

    print("BOT STARTED")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
