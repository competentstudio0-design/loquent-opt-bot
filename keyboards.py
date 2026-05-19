from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

MAIN_KB = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Каталог")],
        [KeyboardButton(text="🛒 Мои заказы")],
        [
            KeyboardButton(
                text="🛍 Открыть магазин",
                web_app=WebAppInfo(
                    url="https://loquent-opt-bot-production.up.railway.app/"
                )
            )
        ]
    ],
    resize_keyboard=True
)
