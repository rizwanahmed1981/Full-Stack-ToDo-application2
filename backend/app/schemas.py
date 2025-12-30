from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    """Base schema for Task"""
    title: str
    description: Optional[str] = None
    completed: bool = False
    user_id: Optional[int] = None

class TaskCreate(TaskBase):
    """Schema for creating a Task"""
    pass

class TaskUpdate(TaskBase):
    """Schema for updating a Task"""
    pass

class TaskRead(TaskBase):
    """Schema for reading a Task"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True