from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def home():
    return open('app/web/static/index.html', encoding='utf-8').read()
