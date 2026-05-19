import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from dotenv import load_dotenv

from google_sheets import products_sheet, orders_sheet
from keyboards import main_keyboard

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Loquent Opt Shop запущен",
        reply_markup=main_keyboard
    )


@dp.message(lambda msg: msg.text == "📦 Каталог")
async def catalog(message: Message):
    products = products_sheet.get_all_records()

    if not products:
        await message.answer("Каталог пуст.")
        return

    for product in products:
        text = (
            f"📦 {product['name']}\n"
            f"💰 Цена: {product['price']} ₽\n"
            f"📦 Остаток: {product['stock']}"
        )

        photo = product.get("photo")

        try:
            if photo:
                await message.answer_photo(photo=photo, caption=text)
            else:
                await message.answer(text)
        except Exception:
            await message.answer(text)


@dp.message(lambda msg: msg.text == "🛒 Мои заказы")
async def my_orders(message: Message):
    orders = orders_sheet.get_all_records()

    user_orders = [
        order for order in orders
        if str(order["user_id"]) == str(message.from_user.id)
    ]

    if not user_orders:
        await message.answer("У тебя пока нет заказов.")
        return

    text = "🛒 Твои заказы:\n\n"

    for order in user_orders:
        text += (
            f"📦 {order['product']}\n"
            f"🔢 Кол-во: {order['quantity']}\n\n"
        )

    await message.answer(text)


async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
