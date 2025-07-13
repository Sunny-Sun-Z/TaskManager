# Task Manager - A Simple Python Project

A command-line task management application built with Python. This project demonstrates fundamental Python concepts and provides a practical example of building a complete application from scratch.

## Features

- ✅ Add new tasks with title, description, and priority
- 📋 View all tasks (completed and pending)
- ✓ Mark tasks as completed
- 🗑️ Delete tasks
- 📊 View task statistics and completion rates
- 💾 Persistent storage (saves tasks to JSON file)
- 🔄 Load tasks automatically when the app starts

## What This Project Teaches

This project covers many fundamental Python concepts:

### Data Structures
- **Lists**: Storing multiple tasks
- **Dictionaries**: Converting tasks to/from JSON format
- **Sets**: Could be used for unique priorities (future enhancement)

### Object-Oriented Programming
- **Classes**: `Task` and `TaskManager` classes
- **Methods**: Instance methods and class methods
- **Constructor**: `__init__` method
- **String representation**: `__str__` method

### Control Flow
- **Loops**: `for` loops for iterating through tasks
- **Conditionals**: `if/elif/else` statements for menu navigation
- **Error handling**: Try/except blocks for file operations

### Functions
- **Function definitions**: Multiple functions for different operations
- **Parameters**: Functions with various parameter types
- **Return values**: Functions that return data

### Modules and File I/O
- **Built-in modules**: `json`, `os`, `datetime`
- **File operations**: Reading and writing JSON files
- **Error handling**: Graceful handling of file errors

## How to Run

1. Make sure you have Python installed on your system
2. Open a terminal/command prompt in the project directory
3. Run the application:

```bash
python task_manager.py
```

## Usage

When you run the application, you'll see a menu with options:

1. **Add a new task**: Create tasks with title, description, and priority
2. **View all tasks**: See all your tasks with their status
3. **Mark task as completed**: Check off completed tasks
4. **Delete a task**: Remove tasks you no longer need
5. **View task statistics**: See completion rates and task counts
6. **Exit**: Close the application

## File Structure

```
task_manager.py    # Main application file
tasks.json        # Data file (created automatically)
README.md         # This documentation file
```

## Data Storage

Tasks are automatically saved to a `tasks.json` file in the same directory. This means:
- Your tasks persist between sessions
- You can close and reopen the app without losing data
- The data is stored in a human-readable JSON format

## Example Task Data

```json
[
  {
    "title": "Learn Python",
    "description": "Complete the basic Python course",
    "priority": "high",
    "completed": false,
    "created_at": "2024-01-15 10:30:00",
    "completed_at": null
  }
]
```

## Learning Objectives

After completing this project, you should understand:

1. **How to structure a Python application** with classes and functions
2. **File I/O operations** for persistent data storage
3. **Error handling** with try/except blocks
4. **User input processing** and validation
5. **Data serialization** (converting objects to/from JSON)
6. **Command-line interface design** with menus and user interaction

## Future Enhancements

Once you're comfortable with this version, you could add:

- Task categories/tags
- Due dates and reminders
- Task search functionality
- Export tasks to different formats
- GUI interface using tkinter
- Database storage instead of JSON files

## Troubleshooting

- **File not found errors**: The app will create the `tasks.json` file automatically
- **Invalid input**: The app handles most input errors gracefully
- **Permission errors**: Make sure you have write permissions in the directory

## Next Steps

After mastering this project:

1. Try adding new features like due dates
2. Experiment with different data storage methods
3. Add unit tests for your functions
4. Create a web version using Flask or Django
5. Build a GUI version using tkinter or PyQt

Happy coding! 🐍
