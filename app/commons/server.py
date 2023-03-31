from fastapi import FastAPI
from app.api.v1.routes import routes as v1_routes
from app.commons.di import Container
from app.api.middlewares.cors import cors
from .config import settings


class Server:
    def __init__(self):
        # set default app
        self.app = FastAPI(middleware=cors())

        # set db and container (dependency injection)
        self.container = Container()
        self.db = self.container.db()  # get db from dependency injection

        @self.app.get("/")
        def root():
            return {
                "name": settings.APP_NAME,
                "stage": settings.APP_ENV
            }

        self.app.include_router(v1_routes)
