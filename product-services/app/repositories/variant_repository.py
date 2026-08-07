from sqlalchemy.orm import Session
from app.models.product_variant import ProductVariant

def create_variant(db:Session, variant:ProductVariant)-> ProductVariant:
    db.add(variant)
    db.commit()
    db.refresh(variant)
    return variant

def get_variant_by_id(db:Session, variant_id: int)-> ProductVariant | None:
    return db.query(ProductVariant).filter(ProductVariant.id == variant_id).first()

def get_variants_by_product_id(db:Session, product_id:int) -> list[ProductVariant]:
    return db.query(ProductVariant).filter(ProductVariant.product_id == product_id).all()


def update_variant(db:Session, variant: ProductVariant) -> ProductVariant:
    db.commit()
    db.refresh(variant)
    return variant

def delete_variant(db:Session, variant:ProductVariant)-> None:
    db.delete(variant)
    db.commit()