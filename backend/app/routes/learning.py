from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database.db import get_db
from models import LearningMaterial
from schemas import LearningMaterialCreate, LearningMaterialResponse

# Learning Assistance Routes
learning_router = APIRouter()


@learning_router.post("/materials", response_model=LearningMaterialResponse, status_code=status.HTTP_201_CREATED)
def add_learning_material(material: LearningMaterialCreate, db: Session = Depends(get_db)):
    db_material = LearningMaterial(
        user_id=material.user_id,
        title=material.title,
        description=material.description,
        content_url=material.content_url,
        entry_text=material.entry_text
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


@learning_router.get("/materials", response_model=List[LearningMaterialResponse])
def get_learning_materials(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(LearningMaterial)
    if user_id is not None:
        query = query.filter(LearningMaterial.user_id == user_id)
    return query.all()
