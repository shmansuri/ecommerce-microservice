from fastapi import APIRouter

router = APIRouter(prefix='/status')

@router.get('/health')
def check_health():
    return{
        "status":"healthy",
        "service": "auth-service"
    }