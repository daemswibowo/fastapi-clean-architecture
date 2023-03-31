from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import as_declarative, declared_attr
from pluralizer import Pluralizer

pluralizer = Pluralizer()


@as_declarative()
class BaseModel:
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return pluralizer.plural(self.__name__.lower())
    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
