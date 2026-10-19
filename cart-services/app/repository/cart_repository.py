from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.cart_item import CartItem
from app.models.cart import Cart

async def get_cart_by_user_id(db:AsyncSession, user_id:int)-> Optional[Cart]:
    stmt = (
        select(Cart)
        .where(Cart.user_id == user_id)
        .options(selectinload(Cart.items))
    )
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def create_cart(db:AsyncSession, user_id:int):
    cart = Cart(user_id=user_id)
    db.add(cart)
    await db.commit()
    await db.refresh(cart, attribute_names='items')
    return cart

async def get_cart_item(db:AsyncSession, cart_id:int, product_id :int) -> Optional[CartItem]:
    stmt = select(CartItem).where(CartItem.cart_id == cart_id, CartItem.product_id == product_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none                                                                   


async def get_item_by_id(db:AsyncSession, id : int) -> Optional[CartItem]:
    stmt = select(CartItem).where(CartItem.id == id )
    result = await db.execute(stmt)
    
    

async def add_cart_item():
    pass

async def update_itme_quantity():
    pass

async def delete_cart_item():
    pass

async def clear_cart_item():
    pass
