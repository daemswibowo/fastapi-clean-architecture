from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from ..data.models.todo_model import Todo
from ..commons.exceptions import NotFoundError


class TodoRepository:
    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self._db = db

    def find_all(self):
        with self._db() as db:
            query = db.query(Todo).all()  # get all todos

            return query

    def find_by_id(self, id: int):
        with self._db() as db:
            query = db.get(Todo, {"id": id})
            if not query:
                raise NotFoundError(detail=f"Not found todo id: {id}")
            return query
