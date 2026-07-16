from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User

def get_user_by_email(email:str, db:Session):
    return db.query(User).filter(User.email == email).first()

    
def create_user(db:Session, user:User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user