from sqlalchemy import orm, create_engine
from app.commons.config import settings

DBTestEngine = create_engine(settings.DATABASE_URI_MAPPER)
DBTestSession = orm.scoped_session(orm.sessionmaker(bind=DBTestEngine))
