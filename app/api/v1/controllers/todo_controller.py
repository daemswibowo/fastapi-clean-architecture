from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from app.commons.di import Container
from app.schemas.todo_schema import TodoResponse
from app.api.v1.services.todo_service import TodoService
from typing import Any

router = APIRouter(prefix="/todos", tags=["todo"])


class WebResponse:
    def __init__(self, data: Any):
        self.data = data


@router.get(
    "",
    response_model=TodoResponse,
    response_description="Todos list successful response",
)
@inject
async def get_todos_list(
    service: TodoService = Depends(Provide[Container.todo_service]),
):
    return {"data": service.get_todos()}


@router.get(
    "/{id}", response_model=TodoResponse, response_description="Find todo by id"
)
@inject
async def find_todo_by_id(
    id: int, service: TodoService = Depends(Provide[Container.todo_service])
):
    return {"data": service.get_todo_by_id(id)}
