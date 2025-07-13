"""
Simple test file for Task Manager
This demonstrates basic testing concepts in Python
"""

import json
import os
import tempfile
from task_manager import Task, TaskManager


def test_task_creation():
    """Test creating a new task"""
    print("Testing task creation...")

    # Create a task
    task = Task("Learn Python", "Complete the basics", "high")

    # Test attributes
    assert task.title == "Learn Python"
    assert task.description == "Complete the basics"
    assert task.priority == "high"
    assert task.completed == False
    assert task.completed_at == None

    print("✓ Task creation test passed!")


def test_task_completion():
    """Test marking a task as completed"""
    print("Testing task completion...")

    task = Task("Test task")
    assert task.completed == False

    # Mark as completed
    task.mark_completed()
    assert task.completed == True
    assert task.completed_at is not None

    print("✓ Task completion test passed!")


def test_task_to_dict():
    """Test converting task to dictionary"""
    print("Testing task to dictionary conversion...")

    task = Task("Test task", "Test description", "medium")
    task_dict = task.to_dict()

    expected_keys = [
        "title",
        "description",
        "priority",
        "completed",
        "created_at",
        "completed_at",
    ]
    for key in expected_keys:
        assert key in task_dict

    assert task_dict["title"] == "Test task"
    assert task_dict["description"] == "Test description"
    assert task_dict["priority"] == "medium"

    print("✓ Task to dictionary test passed!")


def test_task_from_dict():
    """Test creating task from dictionary"""
    print("Testing task from dictionary...")

    task_data = {
        "title": "Test task",
        "description": "Test description",
        "priority": "low",
        "completed": True,
        "created_at": "2024-01-01 12:00:00",
        "completed_at": "2024-01-01 13:00:00",
    }

    task = Task.from_dict(task_data)

    assert task.title == "Test task"
    assert task.description == "Test description"
    assert task.priority == "low"
    assert task.completed == True
    assert task.created_at == "2024-01-01 12:00:00"
    assert task.completed_at == "2024-01-01 13:00:00"

    print("✓ Task from dictionary test passed!")


def test_task_manager():
    """Test TaskManager functionality"""
    print("Testing TaskManager...")

    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        temp_filename = f.name
        print("temp_filename", temp_filename)
    try:
        # Create task manager with temporary file
        manager = TaskManager(temp_filename)

        # Test adding tasks
        manager.add_task("Task 1", "Description 1", "high")
        manager.add_task("Task 2", "Description 2", "medium")

        assert len(manager.tasks) == 2
        assert manager.tasks[0].title == "Task 1"
        assert manager.tasks[1].title == "Task 2"

        # Test marking task as completed
        manager.mark_task_completed(1)
        assert manager.tasks[0].completed == True

        # Test statistics
        # We'll just check that the method doesn't crash
        manager.get_task_stats()

        # Test deleting task
        manager.delete_task(2)
        assert len(manager.tasks) == 1
        assert manager.tasks[0].title == "Task 1"

        print("✓ TaskManager test passed!")

    finally:
        # Clean up temporary file
        if os.path.exists(temp_filename):
            os.remove(temp_filename)


def test_file_operations():
    """Test file save and load operations"""
    print("Testing file operations...")

    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        temp_filename = f.name

    try:
        # Create task manager
        manager = TaskManager(temp_filename)

        # Add some tasks
        manager.add_task("Save test task", "Testing save functionality")
        manager.add_task("Another task", "Second task")

        # Create a new manager instance to test loading
        new_manager = TaskManager(temp_filename)

        # Check that tasks were loaded correctly
        assert len(new_manager.tasks) == 2
        assert new_manager.tasks[0].title == "Save test task"
        assert new_manager.tasks[1].title == "Another task"

        print("✓ File operations test passed!")

    finally:
        # Clean up temporary file
        if os.path.exists(temp_filename):
            os.remove(temp_filename)


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("RUNNING TASK MANAGER TESTS")
    print("=" * 50)

    try:
        test_task_creation()
        test_task_completion()
        test_task_to_dict()
        test_task_from_dict()
        test_task_manager()
        test_file_operations()

        print("\n" + "=" * 50)
        print("🎉 ALL TESTS PASSED! 🎉")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    run_all_tests()
