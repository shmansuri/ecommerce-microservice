from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.repository import cart_repository
from app.schemas.cart_schemas import AddItemRequest, UpdateItemQuantityRequest

def format_cart_response(cart):
    items_data = []
    total_amount = 0.0

    for item in cart.items:
        item_total = round(item.quantity * item.unit_price, 2)
        total_amount += item_total
        items_data.append({
            "id": item.id,
            "product_id": item.product_id,
            "product_name": item.product_name,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
            "total_price": item_total
        })

    return {
        "id": cart.id,
        "user_id": cart.user_id,
        "items": items_data,
        "total_amount": round(total_amount, 2),
        "created_at": cart.created_at,
        "updated_at": cart.updated_at
    }

async def get_or_create_cart(db: AsyncSession, user_id: int):
    cart = await cart_repository.get_cart_by_user_id(db, user_id)
    if not cart:
        cart = await cart_repository.create_cart(db, user_id)
    return format_cart_response(cart)

async def add_item_to_cart(db: AsyncSession, user_id: int, request: AddItemRequest):
    cart = await cart_repository.get_cart_by_user_id(db, user_id)
    if not cart:
        cart = await cart_repository.create_cart(db, user_id)

    existing_item = await cart_repository.get_cart_item(db, cart.id, request.product_id)
    if existing_item:
        new_qty = existing_item.quantity + request.quantity
        await cart_repository.update_item_quantity(db, existing_item, new_qty)
    else:
        await cart_repository.add_cart_item(
            db=db,
            cart_id=cart.id,
            product_id=request.product_id,
            product_name=request.product_name,
            unit_price=request.unit_price,
            quantity=request.quantity
        )

    refreshed_cart = await cart_repository.get_cart_by_user_id(db, user_id)
    return format_cart_response(refreshed_cart)

async def update_item_quantity(db: AsyncSession, user_id: int, item_id: int, request: UpdateItemQuantityRequest):
    cart = await cart_repository.get_cart_by_user_id(db, user_id)
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found")

    item = await cart_repository.get_item_by_id(db, item_id)
    if not item or item.cart_id != cart.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")

    await cart_repository.update_item_quantity(db, item, request.quantity)
    refreshed_cart = await cart_repository.get_cart_by_user_id(db, user_id)
    return format_cart_response(refreshed_cart)

async def remove_item(db: AsyncSession, user_id: int, item_id: int):
    cart = await cart_repository.get_cart_by_user_id(db, user_id)
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found")

    item = await cart_repository.get_item_by_id(db, item_id)
    if not item or item.cart_id != cart.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")

    await cart_repository.delete_cart_item(db, item)
    refreshed_cart = await cart_repository.get_cart_by_user_id(db, user_id)
    return format_cart_response(refreshed_cart)

async def clear_cart(db: AsyncSession, user_id: int):
    cart = await cart_repository.get_cart_by_user_id(db, user_id)
    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found")

    await cart_repository.clear_cart(db, cart)
    return format_cart_response(cart)