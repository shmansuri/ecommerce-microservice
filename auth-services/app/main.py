from fastapi import FastAPI, Request
from .routers import health

app = FastAPI(
    title="Auth Service",
    description="Authentication Microservice",
    version='1.0.0'
)


app.include_router(health.router)


