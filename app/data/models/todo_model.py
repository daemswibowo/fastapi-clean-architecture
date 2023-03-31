from sqlalchemy import Column, Text, BigInteger, Boolean, func, DateTime
from .base_model import BaseModel


class Todo(BaseModel):
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    title = Column(Text, nullable=False)
    is_done = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "is_done": self.is_done,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
