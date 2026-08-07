from fastapi import FastAPI, Request
from .routers import health, auth, user
from app.core.database import Base, SessionLocal, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auth Service",
    description="Authentication Microservice",
    version='1.0.0'
)



app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
