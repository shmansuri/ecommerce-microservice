from sqlalchemy.orm import Session
from app.models.category import Category


def create_category(db: Session, category: Category)-> Category:
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_category_by_id(db:Session, category_id: int) -> Category | None:
    return db.query(Category).filter(Category.id == category_id).first()

def get_category_by_slug(db: Session, slug:str) -> Category | None:
    return db.query(Category).filter(Category.slug == slug).first()

def get_all_categories(db:Session) -> list[Category]:
    return db.query(Category).all()

def update_category(db: Session, category:Category)->Category:
    db.commit()
    db.refresh(category)
    return category
    

def delete_category(db:Session, category:Category)-> None:
    db.delete(category)
    db.commit()
   
