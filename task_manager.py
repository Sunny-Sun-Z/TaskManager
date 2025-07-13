import json
import os
from datetime import datetime


class Task:
    """A simple class to represent a task"""

    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = None

    def mark_completed(self):
        """Mark the task as completed"""
        self.completed = True
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert task to dictionary for JSON storage"""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a task from dictionary data"""
        task = cls(data["title"], data["description"], data["priority"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        task.completed_at = data["completed_at"]
        return task

    def __str__(self):
        status = "✓" if self.completed else "□"
        return f"{status} {self.title} ({self.priority})"


class TaskManager:
    """Main class to manage tasks"""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description="", priority="medium"):
        """Add a new task"""
        task = Task(title, description, priority)
        self.tasks.append(task)
        print(f"Task added: {task.title}")
        self.save_tasks()

    def view_tasks(self, show_completed=True):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found!")
            return

        print("\n" + "=" * 50)
        print("YOUR TASKS")
        print("=" * 50)

        for i, task in enumerate(self.tasks, 1):
            if show_completed or not task.completed:
                print(f"{i}. {task}")
                print(f"   Status: {task.completed}")
                if task.description:
                    print(f"   Description: {task.description}")
                print(f"   Created: {task.created_at}")

                if task.completed and task.completed_at:
                    print(f"   Completed: {task.completed_at}")

                print()

    def mark_task_completed(self, task_index):
        """Mark a task as completed"""
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            if not task.completed:
                task.mark_completed()
                print(f"Task marked as completed: {task.title}")
                self.save_tasks()
            else:
                print("Task is already completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_index):
        """Delete a task"""
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f"Task deleted: {task.title}")
            self.save_tasks()
        else:
            print("Invalid task number!")

    def get_task_stats(self):
        """Get statistics about tasks"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed

        print(f"\nTask Statistics:")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion rate: {completion_rate:.1f}%")

    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.filename, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 30)
    print("TASK MANAGER MENU")
    print("=" * 30)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. View task statistics")
    print("6. Exit")
    print("=" * 30)


def get_user_input(prompt):
    """Get user input with error handling"""
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        exit()


def main():
    """Main function to run the task manager"""
    print("Welcome to Task Manager!")
    print("A simple Python project for managing your tasks.")

    # Create task manager instance
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-6): ")

        if choice == "1":
            title = get_user_input("Enter task title: ")
            if title:
                description = get_user_input("Enter task description (optional): ")
                priority = get_user_input(
                    "Enter priority (low/medium/high) [default: medium]: "
                )
                if not priority:
                    priority = "medium"
                task_manager.add_task(title, description, priority)
            else:
                print("Task title cannot be empty!")

        elif choice == "2":
            show_completed = get_user_input(
                "Show completed tasks? (y/n) [default: y]: "
            ).lower()
            show_completed = show_completed != "n"
            task_manager.view_tasks(show_completed)

        elif choice == "3":
            task_manager.view_tasks(show_completed=False)
            if task_manager.tasks:
                try:
                    task_num = int(
                        get_user_input("Enter task number to mark as completed: ")
                    )
                    task_manager.mark_task_completed(task_num)
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "4":
            task_manager.view_tasks()
            if task_manager.tasks:
                try:
                    task_num = int(get_user_input("Enter task number to delete: "))
                    task_manager.delete_task(task_num)
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "5":
            task_manager.get_task_stats()

        elif choice == "6":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
