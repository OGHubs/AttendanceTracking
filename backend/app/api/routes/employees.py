from typing import Annotated

from app.core.db import get_db
from app.models.employees import Employees
from app.schemas.employees import (
    CreateEmployee,
    ResponseEmployee,
    UpdateEmployee,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/employees/create", response_model=ResponseEmployee)
async def create_employee(
    employee: CreateEmployee, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_employee = Employees(**employee.model_dump())
    db.add(db_employee)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee


@router.put("/employees/update/{employee_id}", response_model=ResponseEmployee)
async def update_employee(
    employee_id: int,
    employee: UpdateEmployee,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    db_employee = await db.get(Employees, employee_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee record not found")

    for key, value in employee.model_dump().items():
        setattr(db_employee, key, value)

    await db.commit()
    await db.refresh(db_employee)
    return db_employee


@router.get("/employees/{employee_id}", response_model=ResponseEmployee)
async def get_employee(employee_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    db_employee = await db.get(Employees, employee_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee record not found")
    return db_employee
