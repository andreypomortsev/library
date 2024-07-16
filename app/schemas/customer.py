from pydantic import ConfigDict, BaseModel
from typing import Optional


class CustomerCreate(BaseModel):
    name: str
    last_name: str
    middle_name: Optional[str] = None
    birth_year: int
    is_author: Optional[bool] = False


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_year: Optional[int] = None
    is_author: Optional[bool] = False


class Customer(BaseModel):
    id: int
    name: str
    last_name: str
    middle_name: Optional[str] = None
    birth_year: int
    is_author: Optional[bool] = False
    model_config = ConfigDict(from_attributes=True)
