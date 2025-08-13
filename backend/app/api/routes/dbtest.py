from fastapi import APIRouter
from app.core.db import SessionLocal
from sqlalchemy import text

router = APIRouter()

@router.get("/test-db")
def test_db_connection():
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
        return {"status": "success", "message": "DB connection is working!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
