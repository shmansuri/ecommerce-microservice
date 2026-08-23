from sqlalchemy.orm import Session
from app.models.product_image import ProductImage

def add_image(db:Session, image:ProductImage)-> ProductImage:
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

def get_image_by_id( db:Session, image_id:int)-> ProductImage:
    return db.query(ProductImage).filter(ProductImage.id == image_id).first()

def get_images_by_product_id(db:Session, product_id:int)-> list[ProductImage]:
    return db.query(ProductImage).filter(ProductImage.product_id == product_id).all()

def delete_image(db: Session, image: ProductImage)-> None:
    db.delete(image)
    db.commit()
