from typing import Optional

from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    author_id: int
    genre: str
    year: int
    status: Optional[bool] = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author_id: Optional[int] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    status: Optional[bool] = True


class Book(BaseModel):
    id: int
    title: str
    author_id: int
    genre: str
    year: int
    status: bool
    model_config = ConfigDict(from_attributes=True)
