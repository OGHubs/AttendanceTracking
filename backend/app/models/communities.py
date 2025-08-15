from datetime import datetime, timezone
from typing import Optional

from app.core.db import Base
from sqlalchemy import DateTime, String
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
