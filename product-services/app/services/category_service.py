from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.category_repository import (
    create_category, 
    update_category, 
    get_all_categories, 
    get_category_by_id,
    get_category_by_name, 
    get_category_by_slug, 
    delete_category,
    search_categories)
from app.models.category import Category



def create_category_service(data, db:Session):
    existing_category = get_category_by_name(db, data.name)
    if existing_category:
        raise HTTPException(status_code=400, detail="category already exist !")

    existing_slug = get_category_by_slug(db, data.slug)

    if existing_slug:
        raise HTTPException(
            status_code=400,
            detail="Category slug already exists!"
        )

    category_obj = Category(**data.model_dump())
    create_category(db, category_obj)
    
    return{
        'status':"success",
        'message': "category create successfully !",
        'data': category_obj
    }

def get_all_categories_service(db:Session, page, limit):
    return get_all_categories(page, limit, db)

def get_category_by_name_service(name:str, db:Session):
    name = get_category_by_name(db, name)
    if not name:
        raise HTTPException(status_code=404, detail='name is not found')
    return name

def get_category_by_id_service(category_id:int, db:Session):
    exist = get_category_by_id(db, category_id)
    if not exist:
        raise HTTPException(status_code=404, detail="Id Not Found")
    return exist

def get_category_by_slug_service(slug:str, db:Session):
    exist = get_category_by_slug(db, slug)
    if not exist:
        raise HTTPException(status_code=404, detail="Slug not found")
    return exist


def category_update_service(category_id:int, data, db:Session):
    fetch_category = get_category_by_id(db, category_id)
    if not fetch_category:
        raise HTTPException(status_code=404, detail="category not found !")

    if data.name is not None:
        exist_name = get_category_by_name(db, data.name)
        if exist_name and exist_name.id != fetch_category.id:
            raise HTTPException(status_code=400, detail="Category already exists!")
        fetch_category.name = data.name


    if data.slug is not None:
        exist_slug = get_category_by_slug(db, data.slug)
        if exist_slug and exist_slug.id != fetch_category.id:
            raise HTTPException(status_code=400, detail= "Category slug already exists! ")

        fetch_category.slug = data.slug


    if data.description is not None:
        fetch_category.description = data.description

    if data.is_active is not None:
        fetch_category.is_active = data.is_active

    update_category(db, fetch_category)
    return{
        'status': "success",
        'message': "Category has been updated successfully !",
        'data': fetch_category
    }

def category_delete_service(category_id:int, db:Session):
    exist_category = get_category_by_id(db, category_id)
    if not exist_category:
        raise HTTPException(status_code=404, detail='category not found !')
    delete_category(db, exist_category) 
    return{
        'status':'success',
        'message':"category successfully deleted",
        'data': exist_category  
    }


def search_category_service(q, page, limit, db:Session):
    return search_categories(db, q, page, limit)