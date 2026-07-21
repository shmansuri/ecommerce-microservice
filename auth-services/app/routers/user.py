from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user

router = APIRouter(prefix='/users')

@router.get('/profile')
async def get_profile(current_user=Depends(get_current_user)):
    return {
        "message":f"Welcome Back {current_user.name}",
        "user":{
            "id":current_user.id,
            "name": current_user.name,
            "email": current_user.email
        }
    }