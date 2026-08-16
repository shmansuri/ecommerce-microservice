from sqlalchemy.orm import Session
from app.models.category import Category
from sqlalchemy import func

def create_category(db: Session, category: Category)-> Category:
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_category_by_id(db:Session, category_id: int) -> Category | None:
    return db.query(Category).filter(Category.id == category_id).first()

def get_category_by_name(db:Session, category_name: str) -> Category | None:
    return db.query(Category).filter(func.lower(Category.name) == category_name.lower()).first()

def get_category_by_slug(db: Session, slug:str) -> Category | None:
    return db.query(Category).filter(func.lower(Category.slug) == slug.lower()).first()

def get_all_categories(page:int, limit:int, db:Session) -> list[Category]:
    offset = (page-1)*limit
    return db.query(Category).offset(offset).limit(limit).all()

def update_category(db: Session, category:Category)->Category:
    db.commit()
    db.refresh(category)
    return category    

def delete_category(db:Session, category:Category)-> None:
    db.delete(category)
    db.commit()
   
def search_categories(db:Session, q:str, page:int, limit:int)-> list[Category]:
    offset = (page-1)*limit
    return db.query(Category).filter(Category.name.ilike(f"%{q}%")).offset(offset).limit(limit).all()