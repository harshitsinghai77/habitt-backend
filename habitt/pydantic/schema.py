import uuid
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class DeepWorkSettingBase(BaseModel):
    daily_goal: int
    daily_report: bool
    notification: bool


class DeepWorkSettingCreate(DeepWorkSettingBase):
    pass


class DeepWorkSetting(DeepWorkSettingBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class DeepWorkProjectBase(BaseModel):
    project_name: str
    user_id: int


class DeepWorkProjectCreate(DeepWorkProjectBase):
    pass


class DeepWorkProject(DeepWorkProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class DeepWorkTaskBase(BaseModel):
    id: int
    user_id: int
    task_description: str


class DeepWorkTaskCreate(DeepWorkTaskBase):
    task_description: str


class DeepWorkTask(DeepWorkTaskBase):
    project_name: List[DeepWorkProject] = []

    class Config:
        orm_mode = True


class DeepWorkDailyTaskBase(BaseModel):
    total_time_allotted: int
    total_time_done: int


class DeepWorkDailyTaskCreate(DeepWorkDailyTaskBase):
    pass


class DeepWorkDailyTask(DeepWorkDailyTaskBase):
    id: int
    user_id: int
    deep_work_task: List[DeepWorkTask] = []

    class Config:
        orm_mode = True


class DeepWorkAnalyticsBase(BaseModel):
    user_id: int
    task_focus_level: int
    task_difficulty: int
    task_notes: str


class DeepWorkAnalyticsCreate(DeepWorkAnalyticsBase):
    pass


class DeepWorkAnalytics(DeepWorkAnalyticsBase):
    id: int

    class Config:
        orm_mode = True


class LastVisitBase(BaseModel):
    last_visit: datetime = None
    days_consecutively_visited: int


class LastVisitCreate(LastVisitBase):
    pass


class LastVisit(LastVisitBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    confirmation: uuid.UUID

    deep_work_setting: List[DeepWorkSetting] = []
    deep_work_project: List[DeepWorkProject] = []
    deep_work_task: List[DeepWorkTask] = []
    deep_work_daily_task: List[DeepWorkDailyTask] = []
    deep_work_analytics: List[DeepWorkAnalytics] = []
    last_visit: List[LastVisit] = []

    class Config:
        orm_mode = True
