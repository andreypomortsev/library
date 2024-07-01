from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class Loan(BaseModel):
    id: int
    book_id: int
    user_id: int
    loan_date: date
    return_date: Optional[date] = Field(default_factory=date.today)


class LoanCreate(BaseModel):
    book_id: int
    user_id: int
    loan_date: Optional[date] = Field(default_factory=date.today)


class LoanUpdate(BaseModel):
    return_date: Optional[date] = Field(default_factory=date.today)
