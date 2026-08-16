from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.product_repository import(
    create_product,
    update_product,
    get_product_by_id,
    get_product_by_slug,
    get_all_products,
    delete_product, 
    search_products,
    get_product_details
)
from app.models.product import Product


def create_product_service(db:Session, data):
    exist_slug = get_product_by_slug(db, data.slug)
    if exist_slug:
        raise HTTPException(status_code=400, detail='Product slug is already exist')
    product = Product(**data.model_dump())
    create_product(db, product)
    return {
        'status':"success",
        'message': 'Product add successfully !',
        'data': product
    }

def get_all_products_service(db:Session, page:int, limit:int):
    return get_all_products(db, page, limit)

def get_product_by_id_service(db:Session, product_id):
    exist_product = get_product_by_id(db, product_id)
    if exist_product is None:
        raise HTTPException(status_code=404, detail="Product is Not Found!")
    return exist_product

def get_product_by_slug_service(db:Session, slug):
    exist_slug = get_product_by_slug(db, slug)
    if exist_slug is None:
        raise HTTPException(status_code=404, detail='Product is Not Found ')
    return exist_slug


def update_product_service(db: Session, product_id: int, data):
    fetch_product = get_product_by_id(db, product_id)

    if fetch_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if data.slug is not None:
        existing_slug = get_product_by_slug(db, data.slug)

        if existing_slug and existing_slug.id != fetch_product.id:
            raise HTTPException(
                status_code=400,
                detail="Product slug already exists"
            )

        fetch_product.slug = data.slug

    if data.name is not None:
        fetch_product.name = data.name

    if data.category_id is not None:
        fetch_product.category_id = data.category_id

    if data.description is not None:
        fetch_product.description = data.description

    if data.is_active is not None:
        fetch_product.is_active = data.is_active

    update_product(db, fetch_product)

    return {
        "status": "success",
        "message": "Product updated successfully!",
        "data": fetch_product
    }

def delete_product_service(db: Session, product_id: int):
    exist_product = get_product_by_id(db, product_id)

    if exist_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    delete_product(db, exist_product)

    return exist_product

def search_product_service(q, page, limit, db:Session):
    return search_products(db, q, page, limit)


def get_product_detail_service(
    product_id: int,
    db: Session
):

    product = get_product_details(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product