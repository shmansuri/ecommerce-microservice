from app.models.order import Order
from sqlalchemy.ext.asyncio import AsyncSession


async def order_create_repositories(data:Order, db:AsyncSession)->Order:
    order = Order(data)
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order
