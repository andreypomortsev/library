from pydantic import BaseModel
from typing import Optional


class AuthorCreate(BaseModel):
    name: str
    last_name: str
    middle_name: Optional[str] = None
    birth_year: int


class AuthorUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_year: Optional[int] = None


class Author(BaseModel):
    id: int
    name: str
    last_name: str
    middle_name: Optional[str] = None
    birth_year: int

    class Config:
        orm_mode = True
