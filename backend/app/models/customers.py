from datetime import datetime, timezone
from typing import Optional

from app.core.db import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class Customers(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    community_id: Mapped[int] = mapped_column(
        ForeignKey("communities.community_id"), index=True
    )
    customer_name: Mapped[str] = mapped_column(String(100))
    customer_role: Mapped[Optional[str]] = mapped_column(String(50), default="attendee")
    customer_email: Mapped[Optional[str]] = mapped_column(String(100))
    customer_mobile_number: Mapped[Optional[str]] = mapped_column(String(12))
    customer_location: Mapped[Optional[str]] = mapped_column(String(500))
    customer_joining_date: Mapped[Optional[datetime]]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
