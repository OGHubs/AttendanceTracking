from datetime import datetime, timezone
from typing import Optional

from app.core.db import Base
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column


class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.event_id"), index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id"), index=True
    )
    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        server_default=func.CURRENT_TIMESTAMP(),
    )
    rating: Mapped[Optional[int]]
    review: Mapped[Optional[str]] = mapped_column(String(500))
    used_qr_registration: Mapped[bool] = mapped_column(default=False)
    check_in_time: Mapped[Optional[datetime]]
    check_out_time: Mapped[Optional[datetime]]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
