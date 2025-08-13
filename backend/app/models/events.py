import enum
from datetime import datetime, timezone
from typing import Optional

from app.core.db import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column


class Events(Base):
    __tablename__ = "events"

    event_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    community_id: Mapped[int] = mapped_column(
        ForeignKey("communities.community_id"), index=True
    )
    event_name: Mapped[str] = mapped_column(String(100))
    event_location: Mapped[Optional[str]] = mapped_column(String(500))
    event_description: Mapped[Optional[str]] = mapped_column(String(500))
    event_gallery: Mapped[Optional[str]] = mapped_column(
        String(500)
    )  # TODO: use apt format
    self_hosted: Mapped[bool] = mapped_column(default=True)
    event_start_time: Mapped[Optional[datetime]]
    event_end_time: Mapped[Optional[datetime]]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )


class EventRegistrations(Base):
    __tablename__ = "event_registrations"

    class RsvpStatus(enum.Enum):
        YES = "yes"
        NO = "no"
        MAYBE = "maybe"

    event_registration_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.event_id"), index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id"), index=True
    )
    rsvp_status: Mapped[Optional[RsvpStatus]]
    event_registration_time: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
