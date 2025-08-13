from typing import Annotated

from app.core.db import get_db
from app.models.events import Events, EventRegistrations
from app.schemas.events import (
    CreateEvent,
    ResponseEvent,
    UpdateEvent,
    CreateEventRegistration,
    ResponseEventRegistration,
    UpdateEventRegistration,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/events/create", response_model=ResponseEvent)
async def create_event(
    event: CreateEvent, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_event = Events(**event.model_dump())
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    return db_event


@router.put("/events/update/{event_id}", response_model=ResponseEvent)
async def update_event(
    event_id: int,
    event: UpdateEvent,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    db_event = await db.get(Events, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event record not found")

    for key, value in event.model_dump().items():
        setattr(db_event, key, value)

    await db.commit()
    await db.refresh(db_event)
    return db_event


@router.get("/events/{event_id}", response_model=ResponseEvent)
async def get_event(event_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    db_event = await db.get(Events, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event record not found")
    return db_event


# Registration routes
@router.post("/event_registrations/create", response_model=ResponseEventRegistration)
async def create_event_registration(
    registration: CreateEventRegistration, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_registration = EventRegistrations(**registration.model_dump())
    db.add(db_registration)
    await db.commit()
    await db.refresh(db_registration)
    return db_registration


@router.put(
    "/event_registrations/update/{registration_id}",
    response_model=ResponseEventRegistration,
)
async def update_event_registration(
    registration_id: int,
    registration: UpdateEventRegistration,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    db_registration = await db.get(EventRegistrations, registration_id)
    if not db_registration:
        raise HTTPException(
            status_code=404, detail="Event registration record not found"
        )

    for key, value in registration.model_dump().items():
        setattr(db_registration, key, value)

    await db.commit()
    await db.refresh(db_registration)
    return db_registration


@router.get(
    "/event_registrations/{registration_id}", response_model=ResponseEventRegistration
)
async def get_event_registration(
    registration_id: int, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_registration = await db.get(EventRegistrations, registration_id)
    if not db_registration:
        raise HTTPException(
            status_code=404, detail="Event registration record not found"
        )
    return db_registration
