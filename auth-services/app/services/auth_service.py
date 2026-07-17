from sqlalchemy.orm import Session
from fastapi import Depends, Response, status,HTTPException
from app.repositories.user_repository import get_user_by_email, create_user
from app.models.user import User
from app.core.password import hash_pwd, verify_hash
from app.core.token import create_access_token, create_refresh_token, verify_token_type, decode_token




async def user_create(data, db:Session):
    already_exist = get_user_by_email(data.email, db)
    if already_exist:
        raise HTTPException(status_code=409, detail="already email exist")
    
    convert_dict = data.model_dump()
    convert_dict["hashed_password"] = hash_pwd(data.password)
    del convert_dict["password"]
    user = User(**convert_dict)
    create_user(db, user)
    return {
        'status':"success",
        "message": "user created successfully",
        "data":user
    }

async def login(data, db:Session):
    user = get_user_by_email(data.email, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if not verify_hash(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='invalid email or password')
    
    access_token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })

    refresh_token = create_refresh_token({
        "sub": str(user.id),
        "email": user.email
    })
    
    return {
        'status': "success",
        'message': "Login successfull",
        'access_token': access_token,
        'refresh_token': refresh_token,
        "token_type": "bearer"

    }

