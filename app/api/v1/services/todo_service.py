from app.repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self, repository: TodoRepository):
        self._repository: TodoRepository = repository

    def get_todos(self):
        return self._repository.find_all()

    def get_todo_by_id(self, id: int):
        return self._repository.find_by_id(id)
