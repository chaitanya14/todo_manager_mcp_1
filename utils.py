from models import TodoItem, TodoList

todo_list = TodoList()

def create_todo_item(title: str, description: str = None, dueDate: str = None) -> dict:
    todo = TodoItem(title, description, dueDate)
    todo_list.add(todo)
    return todo.__dict__

def complete_todo_item(id: str) -> dict:
    updated_item = todo_list.complete(id)
    if updated_item:
        return updated_item.__dict__
    raise ValueError("Todo item not found")

def list_todo_items(status: str) -> list:
    return [todo.__dict__ for todo in todo_list.list(status)]