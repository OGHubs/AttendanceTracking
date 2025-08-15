from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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
