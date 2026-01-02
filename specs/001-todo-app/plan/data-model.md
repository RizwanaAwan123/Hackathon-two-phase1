# Data Model: Phase I Todo Application

**Feature**: Phase I Todo Application
**Created**: 2026-01-01
**Status**: Complete

## Entity: Task

### Fields
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | int | Auto-increment, unique within session | Unique identifier for the task |
| title | str | Required, non-empty | The main task description |
| description | str | Optional, can be empty | Additional details about the task |
| completed | bool | Required | Completion status (True=completed, False=not completed) |

### Implementation
```python
task = {
    'id': int,           # Auto-incrementing integer ID
    'title': str,        # Non-empty string
    'description': str,  # Optional string (can be empty)
    'completed': bool    # Boolean status
}
```

## Data Storage Structure

### Tasks Collection
```python
# In-memory storage
tasks = []      # List of task dictionaries
next_id = 1     # Integer for auto-incrementing ID generation
```

## Validation Rules

### Task Creation Validation
- **Title**: Must be a non-empty string (length > 0)
- **Description**: Optional, can be empty string
- **Completed**: Defaults to False when creating new tasks
- **ID**: Auto-generated, unique within session

### Task Update Validation
- **Title**: If provided, must be non-empty string
- **Description**: Optional, can be updated to empty string
- **ID**: Must exist in current tasks list

### Task Deletion Validation
- **ID**: Must exist in current tasks list

### Task Status Toggle Validation
- **ID**: Must exist in current tasks list

## State Transitions

### Task Lifecycle
```
[New Task Created]
        ↓
[In Progress (completed=False)]
        ↓
[Completed (completed=True)]
        ↓
[Deleted]
```

### State Transition Rules
1. **New Task**: `completed` defaults to `False`
2. **Toggle Status**: `completed` flips from `True` to `False` or `False` to `True`
3. **Update**: Any field except `id` can be modified
4. **Delete**: Task removed from collection entirely

## Business Rules

### ID Generation
- Auto-increment starting from 1
- Sequential numbering within session
- Unique within session scope
- Reset on application restart

### Data Integrity
- No duplicate IDs within session
- Title must not be empty for any task
- Description can be empty or null
- Completion status is boolean only

## Error Conditions

### Invalid States
- Task with empty title
- Task with duplicate ID
- Reference to non-existent task ID

### Validation Failures
- Attempt to update non-existent task
- Attempt to delete non-existent task
- Attempt to toggle status of non-existent task
- Attempt to create task with empty title

## Access Patterns

### Read Operations
- Get all tasks: `get_all_tasks()`
- Get specific task: `get_task_by_id(task_id)`

### Write Operations
- Create task: `add_task(title, description)`
- Update task: `update_task(task_id, title, description)`
- Delete task: `delete_task(task_id)`
- Toggle status: `toggle_task_completion(task_id)`