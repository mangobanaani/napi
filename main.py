from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app import crud, schemas
from app.database import SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.on_event("startup")
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)


@app.get("/events/", response_model=List[schemas.Event])
def get_events(db: Session = Depends(get_db)):
    return crud.get_all_events(db=db)


@app.get("/events/{eid}", response_model=schemas.Event)
def get_event(eid: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, eid=eid)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
