# Implementation Plan: Phase I Todo Application

**Feature**: Phase I Todo Application
**Created**: 2026-01-01
**Status**: Draft
**Based on**: specs/001-todo-app/spec.md

## Technical Context

### Architecture Overview
- **Application Type**: Single-file Python console application
- **Data Storage**: In-memory using Python data structures
- **User Interface**: Menu-driven CLI with numeric input
- **Runtime**: Single session, no persistence beyond runtime
- **Target Python Version**: Python 3.13+

### Core Components
- **Task Manager**: Handles all task operations (CRUD)
- **CLI Handler**: Manages user input and menu display
- **Data Layer**: In-memory storage using Python lists/dicts

### Technology Stack
- **Language**: Python 3.13+
- **Runtime**: Console/terminal
- **No external dependencies**: Pure Python standard library

### Known Unknowns
(All unknowns have been resolved in the research phase)

## Constitution Check

### Compliance Verification
- ✅ Spec-Driven Development: Following approved specification
- ✅ Agent Behavior Rules: No feature invention, following spec only
- ✅ Phase Governance: No future phase concepts included
- ✅ Technology Constraints: Python console app, in-memory only, single file
- ✅ Quality Principles: Clean, readable, beginner-friendly code

### Gates
- **GATE 1**: All functional requirements from spec must be addressed
- **GATE 2**: No violations of constitutional constraints
- **GATE 3**: All error cases from spec must be handled
- **GATE 4**: No database/file persistence implemented

## Phase 0: Research

### Research Tasks
1. **Python Best Practices**: Determine optimal structure for single-file console applications
2. **Input Validation**: Research best practices for CLI input validation in Python
3. **Menu Design**: Best practices for menu-driven console interfaces

### Research Findings

#### Decision: Single-file application structure
**Rationale**: To maintain simplicity as required by the constitution and specification, the application will be structured as a single Python file with clear function separation.
**Alternatives considered**: Multi-file module structure was considered but rejected as it violates the single-file requirement and adds unnecessary complexity for Phase I.

#### Decision: In-memory data storage
**Rationale**: Using Python's built-in list and dict data structures for in-memory task storage meets the specification requirement of no persistence beyond runtime.
**Alternatives considered**: Custom classes vs. simple data structures - simple data structures chosen for beginner-friendliness.

#### Decision: Menu-driven interface
**Rationale**: A numeric menu system provides clear user interaction flow as specified in the requirements.
**Alternatives considered**: Command-line arguments vs. interactive menu - interactive menu chosen as specified in requirements.

## Phase 1: Design & Contracts

### Data Model Design

#### Task Entity Implementation
```python
# Internal representation
task = {
    'id': int,           # Auto-incrementing integer ID
    'title': str,        # Non-empty string
    'description': str,  # Optional string (can be empty)
    'completed': bool    # Boolean status
}
```

#### Data Storage Structure
```python
# In-memory storage
tasks = []  # List of task dictionaries
next_id = 1  # Integer for auto-incrementing ID generation
```

### CLI Control Flow Design

#### Main Application Loop
```
START
├── Display menu options
├── Get user choice
├── Validate choice
├── Execute selected function
├── Handle errors gracefully
├── Loop until exit selected
END
```

#### Menu Options
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

### Functional Requirements Implementation Mapping

| FR Code | Requirement | Implementation |
|---------|-------------|----------------|
| FR-001 | Menu-driven console interface | Display numbered options, process numeric input |
| FR-002 | Auto-incrementing integer IDs | Maintain next_id counter, increment on task creation |
| FR-003 | Non-empty title validation | Check title length > 0 before creating task |
| FR-004 | Optional descriptions | Accept empty descriptions, store as empty string |
| FR-005 | Boolean completion status | Store as True/False in task dictionary |
| FR-006 | Display tasks with details | Format and print all task fields |
| FR-007 | Update task by ID | Find by ID, update title/description fields |
| FR-008 | Delete task by ID | Find by ID, remove from list |
| FR-009 | Toggle completion by ID | Find by ID, flip boolean value |
| FR-010 | Invalid menu handling | Validate input range, show error message |
| FR-011 | Invalid task ID handling | Check ID exists before operations |
| FR-012 | Empty title handling | Validate before task creation |
| FR-013 | Continuous operation | Main loop until exit selected |
| FR-014 | No persistence beyond runtime | Use only in-memory data structures |

### Error Handling Strategy

#### Input Validation
- **Menu selection**: Check if input is numeric and within valid range
- **Task ID**: Verify ID exists in current task list before operations
- **Task title**: Ensure non-empty string when adding tasks

#### Error Response Pattern
- Display clear error message to user
- Return to main menu without crashing
- Continue application execution

#### Specific Error Cases
1. **Empty task list**: Display "No tasks available" message
2. **Invalid task ID**: Display "Task not found" message
3. **Invalid menu choice**: Display "Invalid option" message
4. **Empty task title**: Display "Title cannot be empty" message
5. **Non-numeric input**: Display "Please enter a valid number" message

### Separation of Responsibilities

#### Data Layer Functions
- `add_task(title, description)`
- `get_all_tasks()`
- `get_task_by_id(task_id)`
- `update_task(task_id, title, description)`
- `delete_task(task_id)`
- `toggle_task_completion(task_id)`

#### CLI Layer Functions
- `display_menu()`
- `get_user_choice()`
- `handle_add_task()`
- `handle_view_tasks()`
- `handle_update_task()`
- `handle_delete_task()`
- `handle_toggle_task()`
- `handle_exit()`

#### Main Application Function
- `main()` - orchestrates the application flow

## Phase 2: Implementation Strategy

### Development Approach
1. Implement data layer functions first
2. Implement CLI layer functions
3. Integrate with main application loop
4. Add comprehensive error handling
5. Test all user scenarios

### Quickstart Guide for Implementation
1. Create the single Python file
2. Define the global data structures (tasks list, next_id counter)
3. Implement data layer functions with proper validation
4. Implement CLI functions for each menu option
5. Create main loop with menu display and input processing
6. Add error handling for all edge cases
7. Test all acceptance scenarios

### Code Structure
```
todo_app.py
├── Global variables (tasks, next_id)
├── Data layer functions
├── CLI layer functions
├── Main function
└── Entry point guard
```

## Validation Against Constitution

✅ **All constitutional requirements satisfied**:
- No new features introduced beyond specification
- Single-file implementation approach
- In-memory only storage
- Console-based interface
- No external dependencies
- Beginner-friendly code structure
- Spec-Driven Development: Following approved specification
- Agent Behavior Rules: No feature invention, following spec only
- Phase Governance: No future phase concepts included
- Technology Constraints: Python console app, in-memory only, single file
- Quality Principles: Clean, readable, beginner-friendly code