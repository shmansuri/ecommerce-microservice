from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.product_schema import (
    ProductResponse, 
    ProductCreate, 
    ProductCreateResponse, 
    ProductUpdate,
    ProductListResponse,
    ProductDetailResponse)
from app.services.product_service import(
    get_all_products_service,
    create_product_service,
    update_product_service,
    get_product_by_id_service,
    get_product_by_slug_service,
    delete_product_service,
    search_product_service,
    get_product_detail_service,
)

router = APIRouter(prefix='/product', tags=['products'])


@router.post('/create', response_model=ProductCreateResponse)
async def create_product_router(data:ProductCreate, db:Session = Depends(get_db)):
    return create_product_service(db, data)

@router.get('/all', status_code=200, response_model=list[ProductResponse])
async def get_all_products_router(page:int = Query(1, ge=1), limit: int = Query(20, ge=1, le=100), db:Session = Depends(get_db)):
    return get_all_products_service(db, page, limit)

@router.get('/search', response_model=list[ProductResponse])
async def search_product(q:str, page:int = Query(1, ge=1), limit:int=Query(20, ge=1, le=100), db:Session=Depends(get_db)):
    return search_product_service(q, page, limit, db)

@router.get(
    "/details/{product_id}",
    response_model=ProductDetailResponse
)
async def get_product_detail_router(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_detail_service(product_id, db)

@router.get('/{id}', response_model=ProductResponse)
async def get_product_by_id_router(id:int, db:Session = Depends(get_db)):
    return get_product_by_id_service(db, id)

@router.get('/by-slug/{slug}', response_model=ProductResponse)
async def get_product_by_slug_router(slug:str, db:Session = Depends(get_db)):
    return get_product_by_slug_service(db, slug)

@router.put('/update/{id}', response_model=ProductCreateResponse)
async def update_product_router(product_id:int, data:ProductUpdate,  db:Session = Depends(get_db)):
    return update_product_service(db,product_id, data)

@router.delete('/delete/{id}', response_model=ProductResponse)
async def delete_product_router(id:int, db:Session = Depends(get_db)):
    return delete_product_service(db, id)


