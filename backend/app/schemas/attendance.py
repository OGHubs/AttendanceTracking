from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseAttendance(BaseModel):
    event_id: int
    customer_id: int
    timestamp: datetime
    rating: Optional[int] = None
    review: Optional[str] = None
    used_qr_registration: bool = False
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None


class AttendanceCreate(BaseAttendance):
    pass


class AttendanceUpdate(BaseAttendance):
    used_qr_registration: Optional[bool] = None


class AttendanceResponse(BaseAttendance):
    attendance_id: int
    created_at: datetime
    updated_at: datetime
