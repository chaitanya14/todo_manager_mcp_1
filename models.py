from pydantic import BaseModel
from typing import Optional, List

class Todo(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    due_date: Optional[str] = None
    status: bool
    creation_date: str

class UserTodo(BaseModel):
    user_id: str
    todos: List[Todo]