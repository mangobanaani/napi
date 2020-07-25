from datetime import datetime

from pydantic import BaseModel


# Event schema

class EventBase(BaseModel):
    timestamp: datetime
    emin: str
    emax: str
    event_loc: str


class EventCreate(EventBase):
    timestamp: datetime
    emin: str
    emax: str
    event_loc: str


class Event(EventBase):
    eid: int
    emin: str
    emax: str
    event_loc: str

    class Config:
        orm_mode = True
