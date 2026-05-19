from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

MAIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Каталог")],
        [KeyboardButton(text="🛒 Мои заказы")],
        [
            KeyboardButton(
                text="🛍 Открыть магазин",
                web_app=WebAppInfo(
                    url="https://YOUR-BACKEND-URL/"
                )
            )
        ]
    ],
    resize_keyboard=True
)
