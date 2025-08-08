from typing import Annotated

from app.core.db import get_session
from app.models.attendance import Attendance
from app.schemas.attendance import (AttendanceCreate, AttendanceResponse,
                                    AttendanceUpdate)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/attendance/create", response_model=AttendanceResponse)
async def create_attendance(
    attendance: AttendanceCreate, db: Annotated[AsyncSession, Depends(get_session)]
):
    db_attendance = Attendance(**attendance.model_dump())
    db.add(db_attendance)
    await db.commit()
    await db.refresh(db_attendance)
    return db_attendance


@router.put("/attendance/update/{attendance_id}", response_model=AttendanceResponse)
async def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Annotated[AsyncSession, Depends(get_session)],
):
    db_attendance = await db.get(Attendance, attendance_id)
    if not db_attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    for key, value in attendance.model_dump().items():
        setattr(db_attendance, key, value)

    await db.commit()
    await db.refresh(db_attendance)
    return db_attendance


@router.get("/attendance/{attendance_id}", response_model=AttendanceResponse)
async def get_attendance(
    attendance_id: int, db: Annotated[AsyncSession, Depends(get_session)]
):
    db_attendance = await db.get(Attendance, attendance_id)
    if not db_attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return db_attendance
