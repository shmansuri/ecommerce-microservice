from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.category_schema import CategoryCreate, CategoryCreateResponse, CategoryUpdate, CategoryResponse
from app.services import category_service


router=APIRouter(prefix='/category', tags=['category'])

@router.post('/create', response_model=CategoryCreateResponse, status_code=201)
async def category_create_router(data:CategoryCreate, db:Session = Depends(get_db)):
    return category_service.create_category_service(data, db)

@router.get('/categories', status_code=200)
async def get_all_categoroies_router(db:Session = Depends(get_db)):
    return category_service.get_all_categories_service(db)

@router.get('/by-name/{name}', response_model=CategoryResponse)
async def get_category_by_name_router(name:str, db:Session = Depends(get_db)):
    return category_service.get_category_by_name_service(name, db)

@router.get('/{id}', response_model=CategoryResponse)
async def get_category_by_id_router(id:int, db:Session=Depends(get_db)):
    return category_service.get_category_by_id_service(id, db)

@router.get('/by-slug/{slug}', response_model=CategoryResponse)
async def get_category_by_slug_router(slug:str, db:Session = Depends(get_db)):
    return category_service.get_category_by_slug_service(slug, db)

@router.put('/update/{id}', response_model=CategoryCreateResponse)
async def category_update_router(id:int, data:CategoryUpdate, db:Session = Depends(get_db)):
    return category_service.category_update_service(id, data, db)

@router.delete('/delete/{id}')
async def category_delete_router(id:int, db:Session = Depends(get_db)):
    return category_service.category_delete_service(id, db)