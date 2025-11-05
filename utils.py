from datetime import datetime
from models import Todo

# In-memory storage for todos
_todos = []

def create_todo(title: str, description: str = None, due_date: str = None) -> dict:
    todo_id = str(len(_todos) + 1)
    new_todo = Todo(
        id=todo_id,
        title=title,
        description=description,
        due_date=due_date,
        status=False,
        creation_date=datetime.now().isoformat()
    )
    _todos.append(new_todo)
    return {"message": "Todo created successfully", "todo": new_todo.dict()}

def list_todos(filters: dict = None) -> list:
    if filters:
        completed = filters.get('completed')
        due_soon = filters.get('due_soon')
        filtered_todos = [todo.dict() for todo in _todos if (completed is None or todo.status == completed)]
        return filtered_todos
    return [todo.dict() for todo in _todos]

def complete_todo(todo_id: str) -> dict:
    for todo in _todos:
        if todo.id == todo_id:
            todo.status = True
            return {"message": "Todo marked as complete", "todo": todo.dict()}
    return {"error": "Todo not found"}