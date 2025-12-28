"""Unit tests for the TodoService."""

import pytest
from src.service import TodoService
from src.models import Task


def test_add_task_success():
    """Test adding a task with valid title and description."""
    service = TodoService()

    task = service.add_task("Test Task", "Test Description")

    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False
    assert len(service.get_all_tasks()) == 1
    # Verify ID format
    assert task.id.startswith("tid")
    assert len(task.id) == 5  # "tid" + 2 digits


def test_add_task_empty_title():
    """Test adding a task with empty title raises ValueError."""
    service = TodoService()

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.add_task("")


def test_get_all_tasks():
    """Test getting all tasks."""
    service = TodoService()

    # Add some tasks
    service.add_task("Task 1")
    service.add_task("Task 2")

    tasks = service.get_all_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"
    # Verify ID format for first task
    assert tasks[0].id == "tid01"
    # Verify ID format for second task
    assert tasks[1].id == "tid02"


def test_get_task_by_id_existing():
    """Test getting a task by existing ID."""
    service = TodoService()

    task = service.add_task("Test Task")
    found_task = service.get_task_by_id(task.id)

    assert found_task is not None
    assert found_task.id == task.id
    assert found_task.title == "Test Task"


def test_get_task_by_id_nonexistent():
    """Test getting a task by non-existent ID."""
    service = TodoService()

    task = service.get_task_by_id("non-existent-id")

    assert task is None


def test_delete_task_existing():
    """Test deleting an existing task."""
    service = TodoService()

    task = service.add_task("Test Task")
    result = service.delete_task(task.id)

    assert result is True
    assert len(service.get_all_tasks()) == 0


def test_delete_task_nonexistent():
    """Test deleting a non-existent task."""
    service = TodoService()

    result = service.delete_task("non-existent-id")

    assert result is False
    assert len(service.get_all_tasks()) == 0


def test_delete_task_then_add_again():
    """Test that we can add a new task with the same ID after deletion."""
    service = TodoService()

    # Add first task
    task1 = service.add_task("Task 1")
    # Delete it
    service.delete_task(task1.id)
    # Add another task
    task2 = service.add_task("Task 2")

    # Both tasks should exist
    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Task 2"
    # Verify the new task gets the next ID in sequence
    assert tasks[0].id == "tid02"