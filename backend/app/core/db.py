from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings


engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db(session: Session) -> None:
    # Alembic migrations to be added here
    pass

def db_startup():
    with SessionLocal() as session:
        init_db(session)
