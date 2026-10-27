from fastapi import APIRouter, status, Depends
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.order_schemas import (
    OrderCreate,
    OrderResponse
)

router = APIRouter(prefix='/orders', tags=['orders'])

@router.get('/{id}', response_model=OrderResponse)
async def get_orders_by_id(id:int, db:AsyncSession = Depends(get_db)):
    return id 


@router.post('/create', response_model=OrderResponse)
async def create_order(data:OrderCreate, db:AsyncSession = Depends(get_db)):
    