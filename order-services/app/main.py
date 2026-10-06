from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.router import order_router
from app.core.database import Base, engine



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(title='orders', description='Orders Microservices', version='1.0.0',  lifespan=lifespan)

app.include_router(order_router.router, prefix='/api/v1')

