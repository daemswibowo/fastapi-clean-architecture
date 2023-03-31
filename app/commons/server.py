import os
from fastapi import FastAPI
from app.api.v1.routes import routes as v1_routes
from app.commons.di import Container


class Server:
    def __init__(self):
        # set default app
        self.app = FastAPI()

        # set db and container (dependency injection)
        self.container = Container()
        self.db = self.container.db()  # get db from dependency injection

        # TODO: set cors using cors middleware

        @self.app.get("/")
        def root():
            return {
                "name": "karina-service",
                "stage": os.getenv("APP_ENV")
            }

        self.app.include_router(v1_routes)
