from mcp.server.fastmcp import FastMCP
from models import TodoItem, TodoList
from utils import create_todo_item, complete_todo_item, list_todo_items

mcp = FastMCP(name="Todo MCP Server")

@mcp.tool()
def addTodo(title: str, description: str = None, dueDate: str = None) -> dict:
    """Adds a new todo item to the list."""
    todo_item = create_todo_item(title, description, dueDate)
    return {"message": "Todo item added successfully", "todo": todo_item}

@mcp.tool()
def listTodos(status: str = 'all') -> list:
    """Lists all todo items or filters them by status."""
    return list_todo_items(status)

@mcp.tool()
def completeTodo(id: str) -> dict:
    """Marks a specified todo item as completed."""
    updated_item = complete_todo_item(id)
    return {"message": "Todo item marked as completed", "todo": updated_item}

if __name__ == '__main__':
    mcp.run()