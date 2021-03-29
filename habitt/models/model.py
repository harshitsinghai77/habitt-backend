import datetime
import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from habitt.config.database import Base


class User(Base):
    __tablename__ = "core_user"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    confirmation = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)

    deep_work_setting = relationship("DeepWorkSetting")
    deep_work_project = relationship("DeepWorkProject")
    deep_work_task = relationship("DeepWorkTask")
    deep_work_daily_task = relationship("DeepWorkDailyTask")
    deep_work_analytics = relationship("DeepWorkAnalytics")
    last_visit = relationship("LastVisit")


class DeepWorkSetting(Base):
    __tablename__ = "deepwork_setting"

    id = Column(Integer, primary_key=True)
    daily_goal = Column(Integer, default=4)
    daily_report = Column(Boolean, default=False)
    notification = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("core_user.id"))


class DeepWorkProject(Base):
    __tablename__ = "deepwork_project"

    id = Column(Integer, primary_key=True)
    project_name = Column(String)
    user_id = Column(Integer, ForeignKey("core_user.id"))


class DeepWorkTask(Base):
    __tablename__ = "deepwork_task"

    id = Column(Integer, primary_key=True)
    task_description = Column(Text)
    project_id = Column(Integer, ForeignKey("deepwork_project.id"))
    user_id = Column(Integer, ForeignKey("core_user.id"))

    project = relationship("DeepWorkProject")


class DeepWorkDailyTask(Base):
    __tablename__ = "deepwork_daily_task"

    id = Column(Integer, primary_key=True)
    total_time_allotted = Column(Integer)  # in minutes
    total_time_done = Column(Integer)
    deep_work_task_id = Column(Integer, ForeignKey("deepwork_task.id"))
    user_id = Column(Integer, ForeignKey("core_user.id"))

    deep_work_task = relationship("DeepWorkTask")


class DeepWorkAnalytics(Base):
    __tablename__ = "deepwork_analytics"

    id = Column(Integer, primary_key=True)
    task_focus_level = Column(Integer)
    task_difficulty = Column(Integer)
    task_notes = Column(Text)
    user_id = Column(Integer, ForeignKey("core_user.id"))


class LastVisit(Base):
    __tablename__ = "user_last_visited"

    id = Column(Integer, primary_key=True)
    last_visit = Column(DateTime, default=datetime.datetime.now())
    days_consecutively_visited = Column(Integer)
    user_id = Column(Integer, ForeignKey("core_user.id"))
