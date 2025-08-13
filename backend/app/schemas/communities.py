from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Communities
class BaseCommunity(BaseModel):
    community_name: str
    community_location: Optional[str]
    community_type: str
    community_logo: Optional[str]
    community_description: Optional[str]


class CreateCommunity(BaseCommunity):
    pass


class UpdateCommunity(BaseCommunity):
    community_id: int
    community_name: Optional[str]
    community_type: Optional[str]


class ResponseCommunity(BaseCommunity):
    community_id: int
    created_at: datetime
    updated_at: datetime


# Customers
class BaseCustomer(BaseModel):
    community_id: int
    customer_name: str
    customer_role: Optional[str]
    customer_email: Optional[EmailStr]
    customer_mobile_number: Optional[str]
    customer_location: Optional[str]
    customer_joining_date: Optional[datetime]


class CreateCustomer(BaseCustomer):
    pass


class UpdateCustomer(BaseCustomer):
    customer_id: int
    community_id: Optional[int]
    customer_name: Optional[str]


class ResponseCustomer(BaseCustomer):
    customer_id: int
    created_at: datetime
    updated_at: datetime


# Employees
class BaseEmployee(BaseModel):
    community_id: int
    employee_name: str
    employee_role: str
    employee_email: Optional[EmailStr]
    employee_mobile_number: Optional[str]
    employee_location: Optional[str]
    employee_joining_date: Optional[datetime]


class CreateEmployee(BaseEmployee):
    pass


class UpdateEmployee(BaseEmployee):
    employee_id: int
    employee_role: Optional[str]
    community_id: Optional[int]
    employee_name: Optional[str]


class ResponseEmployee(BaseEmployee):
    employee_id: int
    created_at: datetime
    updated_at: datetime
