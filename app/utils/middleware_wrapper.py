from typing import Optional, List, Type

from fastapi.routing import APIRoute
from starlette.middleware import Middleware


# bind the middleware to an APIRoute subclass
def MiddlewareWrapper(middlewares: Optional[List[Middleware]] = None) -> Type[APIRoute]:
    class CustomAPIRoute(APIRoute):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            app = self.app
            for cls, options in reversed(middlewares or []):
                app = cls(app, **options)
            self.app = app

    return CustomAPIRoute
