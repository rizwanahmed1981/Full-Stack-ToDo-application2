# Data Model: Console Task App

## Task Entity

### Fields
- `id: str` - Unique identifier for the task (UUID string)
- `title: str` - Required title of the task (non-empty validation required)
- `description: str` - Optional description of the task (can be empty)
- `completed: bool` - Status of the task (True for complete, False for incomplete)

### Validation Rules
- Title cannot be empty or None
- ID must be unique within the system
- Description can be empty string if not provided

### State Transitions
- `incomplete` → `complete` when task is marked as done
- `complete` → `incomplete` when task is marked as undone

## Task List Collection

### Structure
- `tasks: List[Task]` - In-memory list storing all tasks
- Maintains order of creation (FIFO)

### Operations
- Add new task to the list
- Find task by ID
- Update existing task
- Remove task by ID
- Retrieve all tasks
- Filter tasks by completion status

## Service Layer Interface

### TodoService Class Responsibilities
- Manage the in-memory tasks list
- Provide CRUD operations for tasks
- Handle business logic validation
- Return appropriate responses to presentation layer

### Required Methods
- `add_task(title: str, description: str = "") -> Task` - Create new task
- `get_all_tasks() -> List[Task]` - Retrieve all tasks
- `get_task_by_id(task_id: str) -> Optional[Task]` - Find specific task
- `update_task(task_id: str, title: str = None, description: str = None) -> bool` - Modify existing task
- `delete_task(task_id: str) -> bool` - Remove task
- `toggle_task_status(task_id: str) -> bool` - Toggle completion status