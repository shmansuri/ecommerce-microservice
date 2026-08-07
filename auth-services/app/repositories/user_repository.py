from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_email(email:str, db:Session):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(id:int, db:Session):
    return db.query(User).filter(User.id == id).first()

    
def create_user(db:Session, user:User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user