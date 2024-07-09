from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.loan import LoanCreate, LoanUpdate, Loan
from services import loan_service
from db.database import get_db

router = APIRouter()


@router.post("/loans/create", response_model=Loan)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    return loan_service.create_loan(loan, db)


@router.put("/loan/{book_id}/edit", response_model=Loan)
def update_loan(book_id: int, loan: LoanUpdate, db: Session = Depends(get_db)):
    return loan_service.update_loan(book_id, loan, db)


@router.get("/loans/", response_model=List[Loan])
def get_all_loans(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return loan_service.get_loans(db, skip, limit)
