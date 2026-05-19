import json
from aiogram import Router, F
from aiogram.types import Message
from app.core.sheets import products, orders

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer('SaaS Shop')

@router.message(F.text == '📦 Каталог')
async def catalog(message: Message):
    for p in products.get_all_records():
        await message.answer(f"{p['name']} {p['price']}")

@router.message(F.web_app_data)
async def webapp(message: Message):
    data = json.loads(message.web_app_data.data)
    orders.append_row([data['user_id'], data['product'], 1])
