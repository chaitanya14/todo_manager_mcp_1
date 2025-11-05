from datetime import datetime
from typing import Optional

class TodoItem:
    def __init__(self, title: str, description: Optional[str], dueDate: Optional[str]):
        self.id = str(datetime.now().timestamp())
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.status = 'pending'
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo: TodoItem):
        self.todos.append(todo)

    def complete(self, id: str):
        for todo in self.todos:
            if todo.id == id:
                todo.status = 'completed'
                todo.updatedAt = datetime.now().isoformat()
                return todo
        return None

    def list(self, status: str):
        if status == 'completed':
            return [todo for todo in self.todos if todo.status == 'completed']
        elif status == 'pending':
            return [todo for todo in self.todos if todo.status == 'pending']
        return self.todos