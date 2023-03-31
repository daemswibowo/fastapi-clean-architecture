import os
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv
from pydantic import BaseSettings, validator

ENV: str = os.getenv("ENV", "dev")

env_path: str = f".{ENV}.env"

if not os.path.exists(os.path.abspath(env_path)):
    # when env file not exists, fall back to original .env file
    env_path: str = ".env"

load_dotenv(env_path)


class Settings(BaseSettings):
    # base
    APP_NAME: str = os.getenv("APP_NAME")
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    API: str = "/api"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "fastapi-clean-architecture"
    DB_ENGINE_MAPPER: dict = {
        "postgresql": "postgresql",
        "mysql": "mysql+pymysql",
    }

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # database
    DB_DIALECT: str = os.getenv("DB_DIALECT", "postgresql")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_DATABASE: str = os.getenv("DB_DATABASE")
    DATABASE_URI: Optional[str] = os.getenv("DATABASE_URI")
    DB_ENGINE: str = DB_ENGINE_MAPPER.get(DB_DIALECT, "postgresql")

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI_MAPPER: str = DATABASE_URI_FORMAT.format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    )

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return (
            f"{values.get('DB_ENGINE')}://{values.get('DB_USER')}:{values.get('DB_PASSWORD')}@"
            f"{values.get('DB_HOST')}:{values.get('DB_PORT')}/{values.get('DB_DATABASE')}"
        )

    # find query
    PAGE = 1
    PAGE_SIZE = 20
    ORDERING = "-id"

    class Config:
        case_sensitive = True


settings = Settings()
