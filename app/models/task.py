from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TaskStatus(enum.Enum):
    open = "open"
    in_progress = "in_progress"
    pending = "pending"
    completed = "completed"

class TaskPriority(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False )  
    description = Column(String, nullable=True  )  
    status = Column(Enum(TaskStatus), default=TaskStatus.open, nullable=False)
    priority = Column(Enum(TaskPriority), default=TaskPriority.low, nullable=False)
    due_date = Column(DateTime)  
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    owner = relationship("User", back_populates="tasks")
