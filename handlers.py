import json

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import MAIN_KB
from google_sheets import products_sheet, orders_sheet

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Магазин запущен",
        reply_markup=MAIN_KB
    )


@router.message(F.text == "📦 Каталог")
async def catalog(message: Message):
    products = products_sheet.get_all_records()

    for p in products:
        await message.answer(
            f"{p['name']}\n💰 {p['price']} ₽"
        )


@router.message(F.web_app_data)
async def webapp(message: Message):
    data = json.loads(message.web_app_data.data)

    orders_sheet.append_row([
        data["user_id"],
        data["product"],
        1
    ])

    await message.answer("✅ Заказ принят")
