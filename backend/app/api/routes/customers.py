from typing import Annotated

from app.core.db import get_db
from app.models.customers import Customers
from app.schemas.customers import (
    CreateCustomer,
    ResponseCustomer,
    UpdateCustomer,
)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


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
