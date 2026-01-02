# Internal API Contracts: Phase I Todo Application

**Feature**: Phase I Todo Application
**Created**: 2026-01-01
**Status**: Complete

## Overview
This document defines the internal function contracts for the Phase I Todo application. These contracts specify the expected inputs, outputs, and behavior of each internal function.

## Data Types

### Task Object
```python
{
    'id': int,           # Auto-incrementing unique identifier
    'title': str,        # Non-empty task title
    'description': str,  # Optional task description (can be empty)
    'completed': bool    # Boolean completion status
}
```

## Function Contracts

### Data Layer Functions

#### `add_task(title: str, description: str = "") -> dict`
- **Purpose**: Create and add a new task to the in-memory storage
- **Inputs**:
  - `title` (str): Non-empty task title
  - `description` (str, optional): Task description, defaults to empty string
- **Output**: The created task dictionary
- **Preconditions**:
  - `title` must be a non-empty string
- **Postconditions**:
  - A new task is added to the tasks list
  - The task has a unique auto-incremented ID
  - The task's completion status is False
- **Side Effects**: Increments the global `next_id` counter
- **Error Conditions**: Raises ValueError if title is empty

#### `get_all_tasks() -> list`
- **Purpose**: Retrieve all tasks from storage
- **Inputs**: None
- **Output**: List of all task dictionaries
- **Preconditions**: None
- **Postconditions**: None
- **Side Effects**: None
- **Error Conditions**: None

#### `get_task_by_id(task_id: int) -> dict or None`
- **Purpose**: Find a specific task by its ID
- **Inputs**:
  - `task_id` (int): The ID of the task to find
- **Output**: Task dictionary if found, None otherwise
- **Preconditions**: None
- **Postconditions**: None
- **Side Effects**: None
- **Error Conditions**: None

#### `update_task(task_id: int, title: str = None, description: str = None) -> bool`
- **Purpose**: Update an existing task's title or description
- **Inputs**:
  - `task_id` (int): ID of the task to update
  - `title` (str, optional): New title if provided
  - `description` (str, optional): New description if provided
- **Output**: True if task was updated, False if task not found
- **Preconditions**:
  - If `title` is provided, it must be non-empty
- **Postconditions**:
  - Task fields are updated if task exists
  - Only specified fields are updated
- **Side Effects**: Modifies existing task in storage
- **Error Conditions**: Returns False if task_id not found; raises ValueError if title is empty

#### `delete_task(task_id: int) -> bool`
- **Purpose**: Remove a task from storage by its ID
- **Inputs**:
  - `task_id` (int): ID of the task to delete
- **Output**: True if task was deleted, False if task not found
- **Preconditions**: None
- **Postconditions**: Task is removed from storage if it existed
- **Side Effects**: Modifies the tasks list
- **Error Conditions**: None

#### `toggle_task_completion(task_id: int) -> bool`
- **Purpose**: Toggle the completion status of a task
- **Inputs**:
  - `task_id` (int): ID of the task to toggle
- **Output**: True if task status was toggled, False if task not found
- **Preconditions**: None
- **Postconditions**: Task's completion status is flipped
- **Side Effects**: Modifies the task's completed field
- **Error Conditions**: None

### CLI Layer Functions

#### `display_menu() -> None`
- **Purpose**: Show the main menu options to the user
- **Inputs**: None
- **Output**: None (writes to console)
- **Preconditions**: None
- **Postconditions**: Menu is displayed to user
- **Side Effects**: Prints menu to stdout
- **Error Conditions**: None

#### `get_user_choice() -> int or None`
- **Purpose**: Get and validate user menu selection
- **Inputs**: None
- **Output**: Integer choice (1-6) or None if invalid input
- **Preconditions**: None
- **Postconditions**: None
- **Side Effects**: Reads input from stdin
- **Error Conditions**: Returns None if input is not a valid integer

#### `handle_add_task() -> None`
- **Purpose**: Handle the task addition workflow
- **Inputs**: None
- **Output**: None
- **Preconditions**: None
- **Postconditions**: A new task may be added to storage
- **Side Effects**: Interacts with user, modifies tasks storage
- **Error Conditions**: May display error messages to user

#### `handle_view_tasks() -> None`
- **Purpose**: Handle displaying all tasks to the user
- **Inputs**: None
- **Output**: None
- **Preconditions**: None
- **Postconditions**: Tasks are displayed to user
- **Side Effects**: Prints task list to stdout
- **Error Conditions**: None

#### `handle_update_task() -> None`
- **Purpose**: Handle the task update workflow
- **Inputs**: None
- **Output**: None
- **Preconditions**: None
- **Postconditions**: A task may be updated in storage
- **Side Effects**: Interacts with user, may modify tasks storage
- **Error Conditions**: May display error messages to user

#### `handle_delete_task() -> None`
- **Purpose**: Handle the task deletion workflow
- **Inputs**: None
- **Output**: None
- **Preconditions**: None
- **Postconditions**: A task may be removed from storage
- **Side Effects**: Interacts with user, may modify tasks storage
- **Error Conditions**: May display error messages to user

#### `handle_toggle_task() -> None`
- **Purpose**: Handle toggling task completion status
- **Inputs**: None
- **Output**: None
- **Preconditions**: None
- **Postconditions**: A task's completion status may be changed
- **Side Effects**: Interacts with user, may modify tasks storage
- **Error Conditions**: May display error messages to user

## Error Handling Contracts

### Validation Rules
1. **Empty Title Validation**: Any operation requiring a title will reject empty strings
2. **Task Existence Validation**: Operations requiring a task ID will check if the task exists
3. **Input Type Validation**: Numeric inputs are validated and converted appropriately

### Error Response Pattern
- Display clear error message to user
- Return to main menu without crashing
- Continue application execution
- Log error details to console if needed for debugging