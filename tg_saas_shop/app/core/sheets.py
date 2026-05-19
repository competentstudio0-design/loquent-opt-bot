import json
import gspread
from google.oauth2.service_account import Credentials
from app.bot.config import GOOGLE_CREDENTIALS, SHEET_ID

products = None
orders = None

def init_sheets():
    global products, orders
    creds = Credentials.from_service_account_info(
        json.loads(GOOGLE_CREDENTIALS),
        scopes=[
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
    )
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID)
    products = sheet.worksheet('products')
    orders = sheet.worksheet('orders')
