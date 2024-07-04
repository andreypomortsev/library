from pydantic import BaseModel
from typing import Optional


# Pydantic схема для добавления книги
class BookCreate(BaseModel):
    title: str
    author_id: int
    genre: str
    year: int
    status: Optional[bool] = True


# Pydantic для изменения книги
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author_id: Optional[int] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    status: Optional[bool] = True


# Pydantic схема для получения книги
class Book(BaseModel):
    id: int
    title: str
    author_id: int
    genre: str
    year: int
    status: bool

    class Config:
        orm_mode = True
