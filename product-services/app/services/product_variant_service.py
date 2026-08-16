from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.product_variant import ProductVariant
from app.repositories.variant_repository import (
    get_variant_by_id,
    get_variants_by_product_id,
    update_variant,
    delete_variant,
    create_variant,
    get_variant_by_sku
)
from app.repositories.product_repository import get_product_by_id


def create_variant_service(data, db:Session):
    existing_sku = get_variant_by_sku(db, data.sku)

    if existing_sku:
        raise HTTPException(
            status_code=400,
            detail="SKU already exists!"
        )

    product = get_product_by_id(db, data.product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found!"
        )

    if data.discount_price is not None and data.discount_price >= data.price:
        raise HTTPException(status_code=400, detail='Discount Price should lesser than the Actual Price !')
    variant = ProductVariant(**data.model_dump())
    create_variant(db, variant)
    return {
        "status":'success',
        'message': "Variant added successfully !",
        'data': variant
    }
    

def get_variant_by_id_service(variant_id, db:Session):
    variant = get_variant_by_id(db, variant_id)

    if variant is None:
        raise HTTPException(
            status_code=404,
            detail="Variant not found!"
        )
    return variant

def update_variant_service(variant_id, data, db:Session):
    exist_variant = get_variant_by_id(db, variant_id)
    if exist_variant is None:
        raise HTTPException(status_code= 404, detail='variant is not found!')

    if data.sku is not None:
        existing_sku = get_variant_by_sku(db, data.sku)
        if existing_sku and existing_sku.id != exist_variant.id:
            raise HTTPException(status_code=400,detail="SKU already exists!")
        exist_variant.sku = data.sku

    new_price = (
        data.price
        if data.price is not None
        else exist_variant.price
    )

    new_discount_price = (
        data.discount_price
        if data.discount_price is not None
        else exist_variant.discount_price
    )

    if new_discount_price is not None and new_discount_price >= new_price:
        raise HTTPException(
            status_code=400,
            detail="Discount price must be less than actual price!"
        )

    if data.price is not None:
        exist_variant.price = data.price

    if data.discount_price is not None:
        exist_variant.discount_price = data.discount_price

    if data.stock is not None:
        exist_variant.stock = data.stock

    if data.attributes is not None:
        exist_variant.attributes = data.attributes

    if data.is_active is not None:
        exist_variant.is_active = data.is_active

    update_variant(db, exist_variant)

    return {
        "status": "success",
        "message": "Variant updated successfully!",
        "data": exist_variant
    }  
    

def get_variants_product_id_service(product_id:int, db:Session):
    product = get_product_by_id(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found!"
        )
    return get_variants_by_product_id(db, product_id)

def delete_variant_service(variant_id:int, db:Session):
    exist_variant = get_variant_by_id(db, variant_id)
    if exist_variant is None:
        raise HTTPException(status_code= 404, detail='variant is not found!')
    delete_variant(db, exist_variant)
    return{
        'status':'success',
        'message': 'variant deleted successfully!',
        'data':exist_variant
    }

def get_variant_by_sku_service(sku: str, db: Session):
    variant = get_variant_by_sku(db, sku)
    if variant is None:
        raise HTTPException(status_code=404,detail="Variant not found!")
    return variant