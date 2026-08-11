from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.services.product_variant_service import (
    get_variant_by_id_service,
    get_variants_product_id_service,
    delete_variant_service,
    update_variant_service,
    create_variant_service,
    get_variant_by_sku_service
)
from app.schemas.variant_schema import (
    VariantCreate,
    VariantResponse,
    VariantUpdate,
    VariantDictResponse
)

router = APIRouter(prefix='/variant', tags=['product_variant'])

@router.post('/create', response_model=VariantDictResponse)
async def create_variant_router(data: VariantCreate, db:Session = Depends(get_db)):
    return create_variant_service(data, db)

@router.get('/{variant_id}', response_model=VariantResponse)
async def get_variant_by_id_router(variant_id:int, db:Session = Depends(get_db)):
    return get_variant_by_id_service(variant_id, db)

@router.get('/product/{product_id}', response_model=VariantResponse)
async def get_variant_by_product_id_router(product_id:int, db:Session = Depends(get_db)):
    return get_variants_product_id_service(product_id, db)

@router.put('/update/{id}', response_model=VariantResponse)
async def update_variant_router(variant_id:int, data:VariantUpdate, db:Session = Depends(get_db)):
    return update_variant_service(variant_id, data, db)

@router.delete('/delete/{id}', response_model=VariantDictResponse)
async def delete_variant_router(variant_id:int, db:Session = Depends(get_db)):
    return delete_variant_service(variant_id, db)

@router.get('/sku/{sku}')
async def get_by_sku_router(sku:str, db:Session = Depends(get_db)):
    return get_variant_by_sku_service(sku, db)