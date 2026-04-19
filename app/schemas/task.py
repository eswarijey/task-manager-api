from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus, TaskPriority


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.open
    priority: Optional[TaskPriority] = TaskPriority.low
    due_date: Optional[datetime] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    due_date: Optional[datetime]
    user_id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
