from datetime import datetime, timezone
from typing import Optional

from app.core.db import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class Communities(Base):
    __tablename__ = "communities"

    community_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    community_name: Mapped[str] = mapped_column(String(100))
    community_location: Mapped[Optional[str]] = mapped_column(String(500))
    community_type: Mapped[str] = mapped_column(String(50))
    community_logo: Mapped[Optional[str]] = mapped_column(
        String(500)
    )  # TODO: use apt format
    community_description: Mapped[Optional[str]] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )


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


class Employees(Base):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    community_id: Mapped[int] = mapped_column(
        ForeignKey("communities.community_id"), index=True
    )
    employee_name: Mapped[str] = mapped_column(String(100))
    employee_role: Mapped[str] = mapped_column(String(50))
    employee_email: Mapped[Optional[str]] = mapped_column(String(100))
    employee_mobile_number: Mapped[Optional[str]] = mapped_column(String(12))
    employee_location: Mapped[Optional[str]] = mapped_column(String(500))
    employee_joining_date: Mapped[Optional[datetime]]
    employee_leaving_date: Mapped[Optional[datetime]]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
