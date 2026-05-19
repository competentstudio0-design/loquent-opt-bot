from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from google_sheets import products_sheet, orders_sheet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def home():
    with open("backend/static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/products")
def products():
    return products_sheet.get_all_records()


@app.post("/order")
def order(data: dict):
    orders_sheet.append_row([
        data["user_id"],
        data["product"],
        1
    ])
    return {"status": "ok"}
