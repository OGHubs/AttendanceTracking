from typing import Annotated

from app.core.db import get_db
from app.models.communities import Communities
from app.schemas.communities import (
    CreateCommunity,
    ResponseCommunity,
    UpdateCommunity,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/communities/create", response_model=ResponseCommunity)
async def create_community(
    community: CreateCommunity, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_community = Communities(**community.model_dump())
    db.add(db_community)
    await db.commit()
    await db.refresh(db_community)
    return db_community


@router.put("/communities/update/{community_id}", response_model=ResponseCommunity)
async def update_community(
    community_id: int,
    community: UpdateCommunity,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    db_community = await db.get(Communities, community_id)
    if not db_community:
        raise HTTPException(status_code=404, detail="Community record not found")

    for key, value in community.model_dump().items():
        setattr(db_community, key, value)

    await db.commit()
    await db.refresh(db_community)
    return db_community


@router.get("/communities/{community_id}", response_model=ResponseCommunity)
async def get_community(
    community_id: int, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_community = await db.get(Communities, community_id)
    if not db_community:
        raise HTTPException(status_code=404, detail="Community record not found")
    return db_community
