from mcp.server.fastmcp import FastMCP
from models import Todo, UserTodo
from utils import create_todo, list_todos, complete_todo

mcp = FastMCP(name="TodoManagerMCP")

@mcp.tool()
def add_todo(title: str, description: str = None, due_date: str = None) -> dict:
    """Adds a new todo item to the list."""
    return create_todo(title, description, due_date)

@mcp.tool()
def list_todos(filters: dict = None) -> list:
    """Lists all todo items with optional filters."""
    return list_todos(filters)

@mcp.tool()
def complete_todo(todo_id: str) -> dict:
    """Marks a specified todo item as complete."""
    return complete_todo(todo_id)

@mcp.resource("/todos")
def manage_todos() -> str:
    """Endpoint for managing todo items."""
    return "Manage todos here"

@mcp.resource("/users/{user_id}/todos")
def user_todos(user_id: str) -> str:
    """Endpoint for managing user-specific todo items."""
    return f"User {user_id} todos here"

if __name__ == '__main__':
    mcp.run()