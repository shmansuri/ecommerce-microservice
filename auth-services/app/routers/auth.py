from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_service import user_create
from app.schemas.auth_schema import RegisterRequested, RegisterResponse, Login
from app.services.auth_service import user_create, login

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/register', response_model=RegisterResponse)
async def user_register(data:RegisterRequested, db:Session = Depends(get_db)):
    return await user_create(data, db)

@router.post('/login')
async def user_login(data: Login, db:Session=Depends(get_db)):
    return await login(data, db)