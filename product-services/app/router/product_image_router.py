from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.product_image_service import (
    create_image_service,
    delete_image_service,
    get_image_by_product_id_service,
    get_image_by_id_service
)
from app.schemas.image_schema import (
    ProductImageCreate,
    ProductImageResponse, 
    ProductImageUpdate
)

router = APIRouter(prefix='/image', tags=['Product Image'])

@router.post('/create', response_model=ProductImageResponse)
async def create_image_router(data:ProductImageCreate, db:Session = Depends(get_db)):
    return create_image_service(data, db)

@router.get('/{id}', response_model=ProductImageResponse)
async def get_image_by_id_router(image_id:int, db:Session = Depends(get_db)):
    return get_image_by_id_service(image_id, db)

@router.get('/product/{product_id}', response_model= ProductImageResponse)
async def get_image_by_product_id_router(product_id:int, db:Session = Depends(get_db)):
    return get_image_by_product_id_service(product_id, db)


@router.put('/update/{id}', response_model=ProductImageUpdate)
async def update_image_router(data, db:Session = Depends(get_db)):
    pass

@router.delete('/delete/{id}', response_model=ProductImageResponse)
async def delete_image_router(image_id:int, db:Session=Depends(get_db)):
    return delete_image_service(image_id, db)