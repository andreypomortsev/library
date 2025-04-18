from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from schemas.loan import LoanCreate, LoanUpdate, Loan
from services import loan_service

router = APIRouter()


@router.post("/loans", response_model=Loan)
async def create_loan(loan: LoanCreate, db: AsyncSession = Depends(get_db)):
    return await loan_service.create_loan(loan, db)


@router.get("/loans", response_model=List[Loan])
async def get_all_loans(
    skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_db)
):
    return await loan_service.get_loans(db, skip, limit)


@router.put("/loans/{book_id}", response_model=Loan)
async def update_loan(
    book_id: int, loan: LoanUpdate, db: AsyncSession = Depends(get_db)
):
    return await loan_service.update_loan(book_id, loan, db)
