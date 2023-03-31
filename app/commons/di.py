from dependency_injector import containers, providers

from app.data.sources.database import Database
from app.commons.config import settings
from app.repositories.todo_repository import TodoRepository
from app.api.v1.services.todo_service import TodoService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.controllers.todo_controller"
        ]
    )

    db = providers.Singleton(Database, url=settings.DATABASE_URI_MAPPER)

    # repositories
    todo_repository = providers.Factory(TodoRepository, db=db.provided.session)

    # services
    todo_service = providers.Factory(TodoService, repository=todo_repository)
