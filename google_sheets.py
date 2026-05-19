# google_sheets.py

import json
import os
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_sheets():
    creds_dict = json.loads(os.getenv("GOOGLE_CREDENTIALS"))

    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(
        "17fAEH1Gn-vpjy90V9dwJGe6ADSQfixdOSBlGTbOb-Lk"
    )

    return (
        spreadsheet.worksheet("products"),
        spreadsheet.worksheet("orders")
    )


products_sheet, orders_sheet = get_sheets()
