from fastapi import APIRouter
from app.api.routes import dbtest


api_router = APIRouter()
api_router.include_router(dbtest.router)
 
