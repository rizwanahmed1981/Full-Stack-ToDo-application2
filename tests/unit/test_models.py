"""Unit tests for the Task model."""

import pytest
from src.models import Task


def test_task_creation():
    """Test creating a Task with valid parameters."""
    task = Task(id="test-id", title="Test Task", description="Test Description", completed=True)

    assert task.id == "test-id"
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is True


def test_task_creation_empty_title():
    """Test creating a Task with empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(id="test-id", title="", description="Test Description", completed=False)


def test_task_creation_none_title():
    """Test creating a Task with None title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(id="test-id", title=None, description="Test Description", completed=False)


def test_task_post_init_validation():
    """Test that Task validation occurs after initialization."""
    # This should work fine
    task = Task(id="test-id", title="Valid Title", description="", completed=False)
    assert task.title == "Valid Title"

    # This should raise ValueError during initialization
    with pytest.raises(ValueError):
        Task(id="test-id", title="", description="", completed=False)