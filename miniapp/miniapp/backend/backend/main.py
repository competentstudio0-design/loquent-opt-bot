from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google_sheets import products_sheet, orders_sheet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 товары для Mini App
@app.get("/products")
def get_products():
    return products_sheet.get_all_records()


# 🛒 заказ из Mini App
@app.post("/order")
def create_order(data: dict):

    orders_sheet.append_row([
        data["user_id"],
        data["product"],
        1
    ])

    return {"status": "ok"}
