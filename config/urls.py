from fastapi import APIRouter
from app.meta import views as meta
from app.api.v1 import views as ethics

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    ethics.router,
    prefix="/api/v1"
)
