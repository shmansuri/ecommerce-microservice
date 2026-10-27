from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services import cart_service
from app.schemas.cart_schemas import (
    CartResponse,
    AddItemRequest,
    UpdateItemQuantityRequest
)

router = APIRouter()

@router.get("/{user_id}", response_model=CartResponse, summary="Get user cart")
async def get_cart(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await cart_service.get_or_create_cart(db, user_id)

@router.post("/{user_id}/items", response_model=CartResponse, status_code=status.HTTP_201_CREATED, summary="Add item to cart")
async def add_item_to_cart(
    user_id: int,
    request: AddItemRequest,
    db: AsyncSession = Depends(get_db)
):
    return await cart_service.add_item_to_cart(db, user_id, request)

@router.put("/{user_id}/items/{item_id}", response_model=CartResponse, summary="Update item quantity")
async def update_item_quantity(
    user_id: int,
    item_id: int,
    request: UpdateItemQuantityRequest,
    db: AsyncSession = Depends(get_db)
):
    return await cart_service.update_item_quantity(db, user_id, item_id, request)

@router.delete("/{user_id}/items/{item_id}", response_model=CartResponse, summary="Remove item from cart")
async def remove_cart_item(
    user_id: int,
    item_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await cart_service.remove_item(db, user_id, item_id)

@router.delete("/{user_id}/clear", response_model=CartResponse, summary="Clear user cart")
async def clear_cart(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await cart_service.clear_cart(db, user_id)