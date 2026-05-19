from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Каталог")],
        [KeyboardButton(text="🛒 Мои заказы")]
    ],
    resize_keyboard=True
)
