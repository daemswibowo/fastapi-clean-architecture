from typing import Generic, TypeVar, Any
from pydantic import BaseModel

T = TypeVar("T", Any, None)


class WebResponse(BaseModel, Generic[T]):
    data: T | None
