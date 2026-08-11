from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.image_repository import (
    add_image,
    get_images_by_product_id,
    delete_image
)

def create_image_service(db:Session, data):
    pass

def get_image_by_id_service(id, db:Session):
    pass

def delete_image_service(id, db:Session):
    pass

def get_image_by_product_id_service(id, db:Session):
    pass

