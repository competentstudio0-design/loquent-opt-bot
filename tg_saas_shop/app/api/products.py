from fastapi import APIRouter
from app.core.sheets import products

router = APIRouter()

@router.get('/products')
def get_products():
    return products.get_all_records()
