from typing import Annotated

from app.core.db import get_db
from app.models.communities import Communities, Customers, Employees
from app.schemas.communities import (
    CreateCommunity,
    ResponseCommunity,
    UpdateCommunity,
    CreateCustomer,
    ResponseCustomer,
    UpdateCustomer,
    CreateEmployee,
    ResponseEmployee,
    UpdateEmployee,
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


@router.post("/customers/create", response_model=ResponseCustomer)
async def create_customer(
    customer: CreateCustomer, db: Annotated[AsyncSession, Depends(get_db)]
):
    db_customer = Customers(**customer.model_dump())
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer


@router.put("/customers/update/{customer_id}", response_model=ResponseCustomer)
async def update_customer(
    customer_id: int,
    customer: UpdateCustomer,
    db: Annotated[AsyncSession, Depends(get_db)],
):
    db_customer = await db.get(Customers, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer record not found")

    for key, value in customer.model_dump().items():
        setattr(db_customer, key, value)

    await db.commit()
    await db.refresh(db_customer)
    return db_customer


@router.get("/customers/{customer_id}", response_model=ResponseCustomer)
async def get_customer(customer_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    db_customer = await db.get(Customers, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer record not found")
    return db_customer


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
