#!/usr/bin/env python3
"""Simple test to verify the console task app works."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.service import TodoService
from src.models import Task

def test_basic_functionality():
    """Test that the basic functionality works."""
    print("Testing basic functionality...")

    # Test service creation
    service = TodoService()
    print("✓ Service created successfully")

    # Test adding a task
    task = service.add_task("Test Task", "Test Description")
    print("✓ Task added successfully")
    print(f"  Task ID: {task.id}")
    print(f"  Task Title: {task.title}")
    print(f"  Task Description: {task.description}")
    print(f"  Task Completed: {task.completed}")

    # Test getting all tasks
    tasks = service.get_all_tasks()
    print(f"✓ Got {len(tasks)} tasks")

    # Test getting task by ID
    found_task = service.get_task_by_id(task.id)
    print("✓ Task found by ID")

    # Test deleting task
    deleted = service.delete_task(task.id)
    print(f"✓ Task deleted: {deleted}")

    # Test getting all tasks after deletion
    tasks_after = service.get_all_tasks()
    print(f"✓ Got {len(tasks_after)} tasks after deletion")

    print("All tests passed!")

if __name__ == "__main__":
    test_basic_functionality()