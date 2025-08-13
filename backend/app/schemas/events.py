from datetime import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class BaseEvent(BaseModel):
    community_id: int
    event_name: str
    event_location: Optional[str]
    event_description: Optional[str]
    event_gallery: Optional[str]
    self_hosted: Optional[bool]
    event_start_time: Optional[datetime]
    event_end_time: Optional[datetime]


class CreateEvent(BaseEvent):
    pass


class UpdateEvent(BaseEvent):
    event_id: int
    community_id: Optional[int]
    event_name: Optional[str]


class ResponseEvent(BaseEvent):
    event_id: int
    created_at: datetime
    updated_at: datetime


class RsvpStatus(Enum):
    YES = "yes"
    NO = "no"
    MAYBE = "maybe"


class BaseEventRegistration(BaseModel):
    event_id: int
    customer_id: int
    rsvp_status: RsvpStatus
    event_registration_time: Optional[datetime]
    updated_at: Optional[datetime]


class CreateEventRegistration(BaseEventRegistration):
    pass


class UpdateEventRegistration(BaseEventRegistration):
    event_registration_id: int
    event_id: Optional[int]
    customer_id: Optional[int]
    rsvp_status: Optional[RsvpStatus]


class ResponseEventRegistration(BaseEventRegistration):
    event_registration_id: int
    event_registration_time: datetime
    updated_at: datetime
