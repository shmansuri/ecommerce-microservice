from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.product_image import ProductImage

from app.repositories.image_repository import (
    add_image,
    get_image_by_id,
    get_images_by_product_id,
    delete_image
)

from app.repositories.product_repository import get_product_by_id


def create_image_service(db: Session, data):

    # print("DB TYPE:", type(db))
    # print("DATA TYPE:", type(data))
    # print("DATA:", data)
    # print("PRODUCT ID:", data.product_id)


    product = get_product_by_id(db, data.product_id)
    # print(product)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found!"
        )

    image = ProductImage(**data.model_dump())

    add_image(db, image)

    return {
        "status": "success",
        "message": "Image added successfully!",
        "data": image
    }
    

def get_image_by_id_service(image_id, db:Session):
    image = get_image_by_id(image_id, db)

    if image is None:
        raise HTTPException(status_code=404, detail='image is not found!')
    return image

def delete_image_service(image_id, db:Session):
    image = get_image_by_id(image_id, db)

    if image is None:
        raise HTTPException(status_code=404, detail='image is not found!')

    delete_image(db, image_id)
    return {
        'status':'success',
        'message': 'Image is successfully deleted!',
        'data': image
    }

def get_image_by_product_id_service(product_id, db:Session):
    product = get_product_by_id(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail='Product not found !')
    return get_images_by_product_id(db, product_id)

