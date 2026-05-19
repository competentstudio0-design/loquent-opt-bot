
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

from google_sheets import sheet

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать"
    )
@dpmessage(Command("catalog"))
async def catalog(message: Message):

    products = sheet.get_all_records()

    text = "📦 Каталог:\n\n"

    for product in products:
        text += (
            f"{product['id']}. "
            f"{product['name']}\n"
            f"💰 {product['price']} ₽\n"
            f"📦 Остаток: {product['stock']}\n\n"
        )

    await message.answer(text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(
        bot,
        skip_updates=True
    )

if __name__ == "__main__":
    asyncio.run(main())

