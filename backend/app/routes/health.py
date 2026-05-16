from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database.db import get_db
from models import MentalHealthEntry
from schemas import MentalHealthEntryCreate, MentalHealthEntryResponse

# Mental Health Monitoring Routes
health_router = APIRouter()


@health_router.post("/entries", response_model=MentalHealthEntryResponse, status_code=status.HTTP_201_CREATED)
def add_health_entry(entry: MentalHealthEntryCreate, db: Session = Depends(get_db)):
    db_entry = MentalHealthEntry(
        user_id=entry.user_id,
        mood=entry.mood,
        notes=entry.notes,
        entry_text=entry.entry_text
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


@health_router.get("/entries", response_model=List[MentalHealthEntryResponse])
def get_health_entries(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(MentalHealthEntry)
    if user_id is not None:
        query = query.filter(MentalHealthEntry.user_id == user_id)
    return query.all()
