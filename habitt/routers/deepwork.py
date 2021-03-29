from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import habitt.models
import habitt.pydantic.schema as schema
from habitt.config.database import SessionLocal
from habitt.services.deepwork import (
    create_deep_work_analytics,
    create_deep_work_project,
    get_deep_work_analytics,
    get_deep_work_project,
)
from habitt.services.user import get_user_by_id

deepwork_router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@deepwork_router.get("/project/{user_id}", response_model=List[schema.DeepWorkProject])
def read_deepwork_project(user_id: int, db: Session = Depends(get_db)):
    project = get_deep_work_project(db, user_id=user_id)
    if project is None:
        raise HTTPException(status_code=404, detail="No project found")
    return project


@deepwork_router.post("/project", response_model=schema.DeepWorkProject)
def create_deepwork_project(
    project: schema.DeepWorkProjectCreate, db: Session = Depends(get_db)
):
    db_user = get_user_by_id(db, user_id=project.user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid `user_id`. No user found")
    db_project = create_deep_work_project(db=db, project=project)
    return db_project


@deepwork_router.get(
    "/analytics/{user_id}", response_model=List[schema.DeepWorkAnalytics]
)
def read_deepwork_project(user_id: int, db: Session = Depends(get_db)):
    project = get_deep_work_analytics(db, user_id=user_id)
    if project is None:
        raise HTTPException(status_code=404, detail="No project found")
    return project


@deepwork_router.post("/analytics", response_model=schema.DeepWorkAnalytics)
def create_deepwork_project(
    analytics: schema.DeepWorkAnalyticsCreate, db: Session = Depends(get_db)
):
    db_user = get_user_by_id(db, user_id=analytics.user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid `user_id`. No user found")
    db_analytics = create_deep_work_analytics(db=db, analytics=analytics)
    return db_analytics
