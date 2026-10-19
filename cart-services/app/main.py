from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import cart, cart_item
from app.router import cart_routes

@asynccontextmanager
async def lifespan(app:FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title='Cart Services',  version="1.0.0", lifespan=lifespan)  

app.include_router(cart_routes.router, prefix='cart', tags=['Cart'])

app.get('/health')
def health_check():
    return {'status':'healthy'}