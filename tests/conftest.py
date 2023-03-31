import pytest
from fastapi.testclient import TestClient
from loguru import logger
from app.commons.di import Container
from app.data.models.base_model import BaseModel
from app.main import app
from app.commons.database_test import DBTestEngine, DBTestSession
from app.commons.config import ENV

if ENV not in ["test"]:
    msg = f"ENV is not test, it is {ENV}"
    pytest.exit(msg)


def reset_db():
    engine = DBTestEngine
    logger.info(engine)
    session = DBTestSession()
    with engine.begin() as conn:
        session.rollback()
        DBTestSession.remove()
        BaseModel.metadata.drop_all(conn)
        BaseModel.metadata.create_all(conn)
    return engine


@pytest.fixture
def client():
    reset_db()
    with TestClient(app) as client:
        yield client


@pytest.fixture
def container():
    return Container()
