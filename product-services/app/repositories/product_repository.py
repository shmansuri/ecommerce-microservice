from sqlalchemy.orm import Session
from app.models.product import Product
from sqlalchemy import func

def create_product(db:Session, product:Product) -> Product:
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_id( db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def get_product_by_slug( db: Session, slug: str) -> Product | None:
    return db.query(Product).filter(Product.slug == slug).first()

def get_all_products(db:Session, page:int, limit:int)-> list[Product]:
    offset = (page-1)*limit
    return {
        db.query(Product).offset(offset).limit(limit).all()
    }

def update_product(db:Session, product:Product) -> Product:
    db.commit()
    db.refresh(product)
    return product

def delete_product(db:Session, product:Product)-> None:
    db.delete(product)
    db.commit()


def search_service(db:Session, q:str, page:int, limit:int)->list[Product]:
    offset = (page-1)*limit
    return{
        db.query(Product).filter(Product.name.ilike(f"{q}")).offset(offset).limit(limit).all()
    }
    