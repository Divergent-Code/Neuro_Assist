from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database.db import get_db
from models import RoutineTask
from schemas import RoutineTaskCreate, RoutineTaskResponse

# Routine Management Routes
routine_router = APIRouter()


@routine_router.post("/tasks", response_model=RoutineTaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(task: RoutineTaskCreate, db: Session = Depends(get_db)):
    db_task = RoutineTask(
        user_id=task.user_id,
        task_name=task.task_name,
        schedule_time=task.schedule_time,
        entry_text=task.entry_text
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@routine_router.get("/tasks", response_model=List[RoutineTaskResponse])
def get_tasks(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(RoutineTask)
    if user_id is not None:
        query = query.filter(RoutineTask.user_id == user_id)
    return query.all()
