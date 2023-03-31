import factory.alchemy
from app.commons.database_test import DBTestSession


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = DBTestSession
        sqlalchemy_session_persistence = 'commit'
