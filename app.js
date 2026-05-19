const tg = window.Telegram.WebApp;
tg.expand();

const products = [
  { name: "Hoodie Black", price: 4990 },
  { name: "T-Shirt White", price: 1990 }
];

const container = document.getElementById("products");

products.forEach(p => {
  const div = document.createElement("div");

  div.className = "card";
  div.innerHTML = `
    <h3>${p.name}</h3>
    <p>${p.price} ₽</p>
    <button onclick="buy('${p.name}')">Купить</button>
  `;

  container.appendChild(div);
});

function buy(name) {
  tg.sendData(JSON.stringify({
    product: name
  }));
}
