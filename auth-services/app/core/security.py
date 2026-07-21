from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.token import decode_token
from app.repositories.user_repository import get_user_by_id

oauth2_scheme  = OAuth2PasswordBearer(tokenUrl='api/v1/auth/login')

def get_current_user(
        token:str = Depends(oauth2_scheme),
        db:Session = Depends(get_db)
    ):
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired toke"
        )
    
    get_user = get_user_by_id(payload["sub"], db)

    if get_user is None:
        raise HTTPException(
            status_code=400,
            detail="user not found"
        )
    
    return get_user
    
