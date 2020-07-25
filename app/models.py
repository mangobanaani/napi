from sqlalchemy import Column, String, Integer, DateTime

from app.database import Base


class Event(Base):
    __tablename__ = "events"

    eid = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    emin = Column(String(32))
    emax = Column(String(32))
    event_loc = Column(Integer)



