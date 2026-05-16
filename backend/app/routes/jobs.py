from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database.db import get_db
from models import JobListing
from schemas import JobListingCreate, JobListingResponse

# Job Listings Routes
jobs_router = APIRouter()


@jobs_router.post("/jobs", response_model=JobListingResponse, status_code=status.HTTP_201_CREATED)
def add_job(job: JobListingCreate, db: Session = Depends(get_db)):
    db_job = JobListing(
        user_id=job.user_id,
        title=job.title,
        company=job.company,
        location=job.location,
        description=job.description,
        entry_text=job.entry_text
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


@jobs_router.get("/jobs", response_model=List[JobListingResponse])
def get_jobs(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(JobListing)
    if user_id is not None:
        query = query.filter(JobListing.user_id == user_id)
    return query.all()
