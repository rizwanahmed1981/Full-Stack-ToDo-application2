"""Business logic for the Console Task App."""

from typing import List, Optional
from src.models import Task


class TodoService:
    """Service class for managing tasks."""

    def __init__(self):
        """Initialize the TodoService with an empty task list."""
        self._tasks: List[Task] = []
        self._id_counter = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the task list.

        Args:
            title: The title of the task
            description: Optional description of the task

        Returns:
            The created Task object

        Raises:
            ValueError: If title is empty
        """
        if not title:
            raise ValueError("Task title cannot be empty")

        task_id = f"tid{self._id_counter:02d}"
        self._id_counter += 1
        task = Task(id=task_id, title=title, description=description, completed=False)
        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.

        Returns:
            List of all Task objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False