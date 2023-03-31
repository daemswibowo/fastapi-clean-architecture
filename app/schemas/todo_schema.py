from datetime import datetime
from typing import List
from pydantic import BaseModel
from .base_schema import WebResponse


class Todo(BaseModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True


class CreateTodo(BaseModel):
    title: str


class TodoResponse(WebResponse):
    data: List[Todo] | Todo | None
