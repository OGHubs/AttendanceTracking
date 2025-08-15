from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


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
