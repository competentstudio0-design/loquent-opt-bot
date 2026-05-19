import json

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import MAIN_KB
from google_sheets import products_sheet, orders_sheet

router = Router()


# 🚀 START
@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Магазин запущен",
        reply_markup=MAIN_KB
    )


# 📦 КАТАЛОГ (через Sheets)
@router.message(lambda m: m.text == "📦 Каталог")
async def catalog(message: Message):

    products = products_sheet.get_all_records()

    if not products:
        await message.answer("Каталог пуст.")
        return

    for p in products:
        await message.answer(
            f"📦 {p['name']}\n💰 {p['price']} ₽\n📦 {p['stock']}"
        )


# 🛒 ЗАКАЗЫ
@router.message(lambda m: m.text == "🛒 Мои заказы")
async def orders(message: Message):

    all_orders = orders_sheet.get_all_records()

    user_orders = [
        o for o in all_orders
        if str(o["user_id"]) == str(message.from_user.id)
    ]

    if not user_orders:
        await message.answer("Заказов нет.")
        return

    text = "🛒 Твои заказы:\n\n"

    for o in user_orders:
        text += f"{o['product']} x{o['quantity']}\n"

    await message.answer(text)


# 🧩 ПРИЁМ ИЗ MINI APP
@router.message(lambda m: m.web_app_data)
async def webapp_handler(message: Message):

    data = json.loads(message.web_app_data.data)

    if data.get("action") == "order":

        orders_sheet.append_row([
            data["user_id"],
            data["product"],
            1
        ])

        await message.answer("✅ Заказ принят из Mini App")
