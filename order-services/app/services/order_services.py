from app.router.order_router import (
    get_orders_by_id,
    create_order
)
from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Order
from app.repositories.order_repositories import (
    order_create_repositories,
)

async def order_create_service(data, db:AsyncSession):
    order = Order(**data.model_dump())
    return await order_create_repositories(order, db)