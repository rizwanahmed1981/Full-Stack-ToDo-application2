"""Data models for the Console Task App."""

from dataclasses import dataclass
from typing import Optional
import uuid


@dataclass
class Task:
    """Represents a task in the task management system."""

    id: str
    title: str
    description: str
    completed: bool

    def __post_init__(self):
        """Validate task fields after initialization."""
        if not self.title:
            raise ValueError("Task title cannot be empty")


def create_task_id() -> str:
    """Generate a unique ID for a task."""
    return str(uuid.uuid4())