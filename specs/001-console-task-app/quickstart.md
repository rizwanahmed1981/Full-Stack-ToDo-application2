# Quickstart Guide: Console Task App

## Prerequisites

- Python 3.13+ installed
- UV package manager (recommended for dependency management)

## Installation

1. Clone the repository
2. Navigate to the project root directory
3. Install dependencies (if any):
   ```
   uv pip install -e .
   ```

## Running the Application

To start the console task manager:
```
python -m src.main
```

## Usage Instructions

Upon launching, you'll see a menu with the following options:
1. **Add Task** - Create a new task with title and optional description
2. **View List** - Display all tasks with ID, Title, Status, and Description
3. **Update Task** - Modify an existing task by ID
4. **Delete Task** - Remove a task by ID
5. **Mark Complete** - Toggle task completion status
6. **Exit** - Quit the application

## Example Workflow

1. **Add Task**: Select option 1, enter a title like "Complete project proposal"
2. **View List**: Select option 2 to see all tasks with their status indicators
3. **Mark Complete**: Select option 5, enter the task ID to mark as complete
4. **Exit**: Select option 6 to quit

## Development Setup

### Testing
Run unit tests:
```
pytest tests/unit/
```

Run integration tests:
```
pytest tests/integration/
```

### Code Quality
All code must follow PEP 8 standards and include type hints for all functions and classes.

## File Structure Overview

```
src/
├── models.py        # Task data model
├── service.py       # Business logic (TodoService)
├── main.py          # CLI interface and application loop
└── __init__.py      # Package initialization

tests/
├── unit/
│   ├── test_models.py
│   └── test_service.py
└── integration/
    └── test_cli.py
```

## Error Handling

The application provides clear error messages for:
- Empty task titles
- Invalid task IDs
- Attempting operations on non-existent tasks