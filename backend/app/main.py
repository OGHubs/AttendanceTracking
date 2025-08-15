from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.core.db import Base, engine
from app.api.main import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)
app.include_router(api_router, prefix=settings.API_V1_STR)
