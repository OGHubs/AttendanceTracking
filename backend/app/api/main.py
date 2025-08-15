from fastapi import APIRouter
from app.api.routes import dbtest, attendance, communities, events, customers, employees


api_router = APIRouter()
api_router.include_router(dbtest.router)
api_router.include_router(attendance.router)
api_router.include_router(communities.router)
api_router.include_router(customers.router)
api_router.include_router(employees.router)
api_router.include_router(events.router)
