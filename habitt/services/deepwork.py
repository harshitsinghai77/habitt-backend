from sqlalchemy.orm import Session

import habitt.models.model as model
import habitt.pydantic.schema as schema


def get_deep_work_task(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DeepWorkTask).offset(skip).limit(limit).all()


def create_deep_work_task(
    db: Session,
    deepwork_task: schema.DeepWorkTaskCreate,
    user_id: int,
    project_id: int,
):
    db_deep_work_task = models.DeepWorkTask(
        **deepwork_task.dict(), user_id=user_id, project_id=project_name
    )
    db.add(db_deep_work_task)
    db.commit()
    db.refresh(db_item)
    return db_deep_work_task


def get_deep_work_project(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(model.DeepWorkProject)
        .filter(user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_deep_work_project(db: Session, project: schema.DeepWorkProjectCreate):
    db_project = model.DeepWorkProject(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_deep_work_analytics(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(model.DeepWorkAnalytics)
        .filter(user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_deep_work_analytics(db: Session, analytics: schema.DeepWorkAnalyticsCreate):
    db_analytics = model.DeepWorkAnalytics(**analytics.dict())
    db.add(db_analytics)
    db.commit()
    db.refresh(db_analytics)
    return db_analytics
