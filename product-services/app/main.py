from fastapi import FastAPI
from app.core.database import Base, engine
from app.router import category_router, product_router, product_image_router, product_variant_router



Base.metadata.create_all(bind=engine)


app = FastAPI(title="Product Services", description="Product microservices", version='1.0.0')

app.include_router(category_router.router, prefix='/api/v1')
app.include_router(product_router.router, prefix='/api/v1')
app.include_router(product_variant_router.router, prefix='/api/v1')
app.include_router(product_image_router.router, prefix='/api/v1')