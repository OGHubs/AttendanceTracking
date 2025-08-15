from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


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
