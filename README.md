# TodoManagerMCP

## Description
An MCP server for managing todo items with add, list, and complete operations.

## Installation
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.

## Usage
Run the server with `python -m todo_manager_mcp`.

## API Endpoints
- `/todos`: Manage todo items.
- `/users/{user_id}/todos`: Manage user-specific todo items.

## Tools
- `add_todo`: Adds a new todo item.
- `list_todos`: Lists all todo items with optional filters.
- `complete_todo`: Marks a specified todo item as complete.