import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

from google_sheets import sheet

TOKEN = os.getenv("8816584489:AAGTqxu-ySW-DkpYhQeunyWBUXJK5jOwJYo")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать в LOQUENT OPT!"
    )


@dp.message(Command("catalog"))
async def catalog_handler(message: Message):

    products = sheet.get_all_records()

    if not products:
        await message.answer("Каталог пуст.")
        return

    text = "📦 <b>Каталог товаров:</b>\n\n"

    for product in products:
        text += (
            f"🆔 {product['id']}\n"
            f"📦 {product['name']}\n"
            f"💰 Цена: {product['price']} ₽\n"
            f"📦 Остаток: {product['stock']}\n\n"
        )

    await message.answer(text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
