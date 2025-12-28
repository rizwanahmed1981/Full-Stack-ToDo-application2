# Console Task App

A simple console-based task management application built with Python featuring a modern Rich UI.

## Features

- Add tasks with title and optional description
- View all tasks with ID, Title, Status, and Description in a rich table format
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete with visual indicators
- Clean exit functionality
- Enhanced user interface with Rich styling

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

Run the application:
```bash
python -m src.main
```

Or using the installed command:
```bash
taskapp
```

## Development

### Running Tests

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/
```

### Project Structure

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

## Contributing

This project follows the Speckit Constitution which emphasizes:
- Clean Architecture with separation of concerns
- Python 3.13+ with UV package manager
- In-memory storage for current phase
- PEP 8 compliance with type hints and docstrings
- Testable logic via pytest