# Quickstart Guide: Phase I Todo Application

**Feature**: Phase I Todo Application
**Created**: 2026-01-01
**Status**: Complete

## Overview
This guide provides the essential information needed to implement the Phase I Todo application according to the specification and plan.

## Prerequisites
- Python 3.13+ installed
- Basic understanding of Python functions and data structures
- Console/terminal access

## Implementation Steps

### Step 1: Set Up the Basic Structure
Create a single Python file named `todo_app.py` with the following structure:

```python
#!/usr/bin/env python3
"""
Todo Application - Phase I
A console-based todo application with in-memory storage.
"""

# Global variables
tasks = []  # List to store all tasks
next_id = 1  # Counter for auto-incrementing task IDs

def main():
    """Main application function"""
    print("Welcome to the Todo Application!")
    # Main loop implementation goes here

if __name__ == "__main__":
    main()
```

### Step 2: Implement the Task Data Model
Add the task management functions:

```python
def add_task(title, description=""):
    """Add a new task to the list"""
    global next_id
    task = {
        'id': next_id,
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    next_id += 1
    return task

def get_all_tasks():
    """Return all tasks"""
    return tasks

def get_task_by_id(task_id):
    """Find a task by its ID"""
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def update_task(task_id, title=None, description=None):
    """Update a task's title or description"""
    task = get_task_by_id(task_id)
    if task:
        if title is not None:
            task['title'] = title
        if description is not None:
            task['description'] = description
        return True
    return False

def delete_task(task_id):
    """Delete a task by ID"""
    global tasks
    task = get_task_by_id(task_id)
    if task:
        tasks = [t for t in tasks if t['id'] != task_id]
        return True
    return False

def toggle_task_completion(task_id):
    """Toggle the completion status of a task"""
    task = get_task_by_id(task_id)
    if task:
        task['completed'] = not task['completed']
        return True
    return False
```

### Step 3: Implement CLI Functions
Add the user interface functions:

```python
def display_menu():
    """Display the main menu options"""
    print("\n--- Todo Application ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("------------------------")

def get_user_choice():
    """Get and validate user menu choice"""
    try:
        choice = int(input("Enter your choice (1-6): "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        return None

def handle_add_task():
    """Handle adding a new task"""
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty!")
        return

    description = input("Enter task description (optional): ").strip()
    add_task(title, description)
    print("Task added successfully!")

def handle_view_tasks():
    """Handle viewing all tasks"""
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Task List ---")
    for task in tasks:
        status = "✓" if task['completed'] else "○"
        print(f"{status} [{task['id']}] {task['title']}")
        if task['description']:
            print(f"    Description: {task['description']}")
    print("-----------------")

def handle_update_task():
    """Handle updating a task"""
    if not tasks:
        print("No tasks available to update.")
        return

    try:
        task_id = int(input("Enter task ID to update: "))
        task = get_task_by_id(task_id)
        if not task:
            print("Task not found!")
            return

        new_title = input(f"Enter new title (current: {task['title']}), or press Enter to keep current: ").strip()
        new_description = input(f"Enter new description (current: {task['description']}), or press Enter to keep current: ").strip()

        # Update only if user provided new values
        update_needed = False
        if new_title:
            if new_title != task['title']:  # Only update if different
                if new_title.strip():  # Validate non-empty
                    task['title'] = new_title
                    update_needed = True
                else:
                    print("Error: Task title cannot be empty!")
                    return
        if new_description or (new_description == ""):  # Allow empty description
            if new_description != task['description']:  # Only update if different
                task['description'] = new_description
                update_needed = True

        if update_needed:
            print("Task updated successfully!")
        else:
            print("No changes made.")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def handle_delete_task():
    """Handle deleting a task"""
    if not tasks:
        print("No tasks available to delete.")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
        if delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Task not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def handle_toggle_task():
    """Handle toggling task completion status"""
    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to toggle: "))
        if toggle_task_completion(task_id):
            task = get_task_by_id(task_id)
            status = "completed" if task['completed'] else "incomplete"
            print(f"Task marked as {status}!")
        else:
            print("Task not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")
```

### Step 4: Complete the Main Function
Implement the main application loop:

```python
def main():
    """Main application function"""
    print("Welcome to the Todo Application!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_add_task()
        elif choice == 2:
            handle_view_tasks()
        elif choice == 3:
            handle_update_task()
        elif choice == 4:
            handle_delete_task()
        elif choice == 5:
            handle_toggle_task()
        elif choice == 6:
            print("Thank you for using the Todo Application!")
            break
        else:
            if choice is not None:  # Only show error if it was a number but out of range
                print("Invalid choice! Please select a number between 1 and 6.")

        # Pause to let user see results before showing menu again
        input("\nPress Enter to continue...")
```

### Step 5: Test All Scenarios
Verify the implementation against all acceptance criteria:
- Add multiple tasks
- View all tasks with status
- Update task title/description
- Delete task by ID
- Toggle task completion status
- Handle invalid inputs gracefully

## Key Implementation Notes

1. **Global Variables**: Use global variables for `tasks` list and `next_id` counter to maintain state
2. **Error Handling**: Wrap user input in try-except blocks to handle invalid numeric input
3. **Validation**: Check for empty titles when adding/updating tasks
4. **User Experience**: Provide clear prompts and messages for all operations
5. **Graceful Exit**: Allow the application to exit cleanly when option 6 is selected

## File Structure
The final implementation should be in a single file: `todo_app.py`