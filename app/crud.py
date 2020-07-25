from sqlalchemy.orm import Session

import app.schemas as schemas
from app.models import Event


# Event

def create_event(db: Session, event: schemas.EventCreate):
    obj = Event(**event.dict())
    db.add(obj)
    db.commit()
    return obj


def get_all_events(db: Session):
    return db.query(Event).all()


def get_event(db: Session, eid):
    return db.query(Event).filter(Event.eid == eid).first()


def edit_event(db: Session, eid, event: schemas.EventCreate):
    obj = db.query(Event).filter(Event.eid == eid).first()
    obj.emin = event.emin
    obj.emax = event.emax
    obj.timestamp = event.timestamp
    db.commit()
    return obj


def delete_event(db: Session, eid):
    db.query(Event).filter(Event.eid == eid).delete()
    db.commit()
