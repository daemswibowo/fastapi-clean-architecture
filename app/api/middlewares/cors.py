from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from app.commons.config import settings


def cors():
    origins = settings.BACKEND_CORS_ORIGINS

    return [
        Middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
    ]
