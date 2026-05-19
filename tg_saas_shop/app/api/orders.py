from fastapi import APIRouter
from app.core.sheets import orders

router = APIRouter()

@router.post('/order')
def order(data: dict):
    orders.append_row([data['user_id'], data['product'], 1])
    return {'status': 'ok'}
