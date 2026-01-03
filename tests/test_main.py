"""Tests for the Todo CLI Application core functionality.

This test suite covers:
- Add Task
- View Task List
- Update Task
- Delete Task
- Mark Task Complete/Incomplete
"""

import unittest
import sys
import os

# Add src directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.task import Task
from services.task_repository import TaskRepository, TaskNotFoundError, InvalidDescriptionError


class TestTaskRepository(unittest.TestCase):
    """Test the TaskRepository class functionality."""

    def setUp(self):
        """Set up a fresh TaskRepository for each test."""
        self.repo = TaskRepository()

    def test_add_task(self):
        """Test adding a new task."""
        task = self.repo.add("Test task description")

        # Verify task was created with correct properties
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task description")
        self.assertFalse(task.is_complete)

        # Verify task is stored in repository
        retrieved_task = self.repo.get(1)
        self.assertEqual(retrieved_task.id, task.id)
        self.assertEqual(retrieved_task.description, task.description)
        self.assertEqual(retrieved_task.is_complete, task.is_complete)

    def test_view_task_list(self):
        """Test viewing all tasks."""
        # Add multiple tasks
        task1 = self.repo.add("First task")
        task2 = self.repo.add("Second task")
        task3 = self.repo.add("Third task")

        # Get all tasks
        all_tasks = self.repo.get_all()

        # Verify all tasks are returned
        self.assertEqual(len(all_tasks), 3)
        self.assertEqual(all_tasks[0].id, 1)
        self.assertEqual(all_tasks[1].id, 2)
        self.assertEqual(all_tasks[2].id, 3)
        self.assertEqual(all_tasks[0].description, "First task")
        self.assertEqual(all_tasks[1].description, "Second task")
        self.assertEqual(all_tasks[2].description, "Third task")

    def test_update_task(self):
        """Test updating a task's description."""
        # Add a task first
        original_task = self.repo.add("Original description")

        # Update the task
        updated_task = self.repo.update(1, "Updated description")

        # Verify the task was updated
        self.assertEqual(updated_task.id, 1)
        self.assertEqual(updated_task.description, "Updated description")
        self.assertFalse(updated_task.is_complete)

        # Verify the change is persisted in the repository
        retrieved_task = self.repo.get(1)
        self.assertEqual(retrieved_task.description, "Updated description")

    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist."""
        with self.assertRaises(TaskNotFoundError):
            self.repo.update(999, "New description")

    def test_delete_task(self):
        """Test deleting a task."""
        # Add tasks
        task1 = self.repo.add("Task to delete")
        task2 = self.repo.add("Another task")

        # Delete the first task
        self.repo.delete(1)

        # Verify the task is deleted
        deleted_task = self.repo.get(1)
        self.assertIsNone(deleted_task)

        # Verify the second task still exists
        remaining_task = self.repo.get(2)
        self.assertIsNotNone(remaining_task)
        self.assertEqual(remaining_task.description, "Another task")

    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist."""
        with self.assertRaises(TaskNotFoundError):
            self.repo.delete(999)

    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        # Add a task
        task = self.repo.add("Incomplete task")

        # Verify initial state
        self.assertFalse(task.is_complete)

        # Toggle to complete
        completed_task = self.repo.toggle_complete(1)

        # Verify task is now complete
        self.assertTrue(completed_task.is_complete)

        # Verify change is persisted
        retrieved_task = self.repo.get(1)
        self.assertTrue(retrieved_task.is_complete)

    def test_mark_task_incomplete(self):
        """Test marking a completed task as incomplete."""
        # Add a task and mark it complete
        task = self.repo.add("Complete task")
        completed_task = self.repo.toggle_complete(1)
        self.assertTrue(completed_task.is_complete)

        # Toggle back to incomplete
        incomplete_task = self.repo.toggle_complete(1)

        # Verify task is now incomplete
        self.assertFalse(incomplete_task.is_complete)

        # Verify change is persisted
        retrieved_task = self.repo.get(1)
        self.assertFalse(retrieved_task.is_complete)

    def test_toggle_nonexistent_task(self):
        """Test toggling completion status of a task that doesn't exist."""
        with self.assertRaises(TaskNotFoundError):
            self.repo.toggle_complete(999)

    def test_task_validation(self):
        """Test task description validation."""
        # Test empty description
        with self.assertRaises(InvalidDescriptionError):
            self.repo.add("")

        # Test whitespace-only description
        with self.assertRaises(InvalidDescriptionError):
            self.repo.add("   ")

        # Test description with leading/trailing whitespace (should be stripped)
        task = self.repo.add("  Task with spaces  ")
        self.assertEqual(task.description, "Task with spaces")

        # Test long description (should be truncated)
        long_description = "x" * 501  # 501 characters
        task = self.repo.add(long_description)
        self.assertEqual(len(task.description), 500)  # Should be truncated to 500

    def test_task_id_sequentiality(self):
        """Test that task IDs are assigned sequentially and not reused."""
        # Add tasks
        task1 = self.repo.add("First task")
        task2 = self.repo.add("Second task")
        task3 = self.repo.add("Third task")

        # Verify sequential IDs
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        # Delete middle task
        self.repo.delete(2)

        # Add another task - should get next ID, not reuse deleted ID
        task4 = self.repo.add("Fourth task")
        self.assertEqual(task4.id, 4)

    def test_count_tasks(self):
        """Test counting complete and incomplete tasks."""
        # Add tasks
        self.repo.add("Incomplete task 1")
        self.repo.add("Incomplete task 2")
        self.repo.add("Complete task")

        # Mark one task as complete
        self.repo.toggle_complete(3)

        # Count tasks
        complete_count, incomplete_count = self.repo.count()

        self.assertEqual(complete_count, 1)
        self.assertEqual(incomplete_count, 2)


if __name__ == '__main__':
    unittest.main()