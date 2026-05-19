from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from google_sheets import products_sheet, orders_sheet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 MINI APP (HTML)
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
</head>
<body>

<h2>🛍 Магазин</h2>

<div id="products"></div>

<script>
const tg = window.Telegram.WebApp;
tg.expand();

async function loadProducts() {
  const res = await fetch("/products");
  const products = await res.json();

  const container = document.getElementById("products");

  products.forEach(p => {
    const div = document.createElement("div");

    div.innerHTML = `
      <hr>
      <b>${p.name}</b><br>
      💰 ${p.price} ₽<br>
      📦 ${p.stock}<br>
      <button onclick='buy("${p.name}")'>Купить</button>
    `;

    container.appendChild(div);
  });
}

function buy(name) {
  tg.sendData(JSON.stringify({
    action: "order",
    product: name,
    user_id: tg.initDataUnsafe?.user?.id
  }));
}

loadProducts();
</script>

</body>
</html>
"""

# 📦 товары
@app.get("/products")
def get_products():
    return products_sheet.get_all_records()


# 🛒 заказ
@app.post("/order")
async def create_order(request: Request):
    data = await request.json()

    orders_sheet.append_row([
        data["user_id"],
        data["product"],
        1
    ])

    return {"status": "ok"}
