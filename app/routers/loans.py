from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from schemas.loan import LoanCreate, LoanUpdate, Loan
from db.models import Loan as DBLoan
from db.database import get_db

router = APIRouter()


@router.post("/loans/create", response_model=Loan)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    try:
        query = text("SELECT create_book_loan(:book_id, :user_id, :loan_date)")
        db.execute(
            query,
            {
                "book_id": loan.book_id,
                "user_id": loan.user_id,
                "loan_date": loan.loan_date,
            },
        )
        db.commit()
        query = text(
            "SELECT * FROM loans WHERE book_id = :book_id AND \
                return_date IS NULL ORDER BY id DESC LIMIT 1"
        )
        new_loan = db.execute(query, {"book_id": loan.book_id}).fetchone()._asdict()

        if not new_loan:
            msg = "Не удалось найти информацию."
            raise HTTPException(status_code=404, detail=msg)
        response = Loan(
            id=new_loan["id"],
            book_id=new_loan["book_id"],
            user_id=new_loan["user_id"],
            loan_date=new_loan["loan_date"],
            return_date=new_loan["return_date"],
        )
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/loans/{book_id}/edit", response_model=Loan)
def update_loan(book_id: int, loan: LoanUpdate, db: Session = Depends(get_db)):
    try:
        close_query = text("SELECT return_book(:book_id, :return_date)")
        params = {"book_id": book_id, "return_date": loan.return_date}
        db.execute(close_query, params)
        db.commit()
        query = text(
            "SELECT * FROM loans WHERE book_id = :book_id AND \
                return_date IS NOT NULL ORDER BY id DESC LIMIT 1"
        )
        closed_loan = db.execute(query, {"book_id": book_id}).fetchone()._asdict()

        if not closed_loan:
            msg = "Не удалось найти информацию."
            raise HTTPException(status_code=404, detail=msg)

        response = Loan(
            id=closed_loan["id"],
            book_id=closed_loan["book_id"],
            user_id=closed_loan["user_id"],
            loan_date=closed_loan["loan_date"],
            return_date=closed_loan["return_date"],
        )
        return response

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/loans/", response_model=List[Loan])
def get_all_loans(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    loans = db.query(DBLoan).offset(skip).limit(limit).all()
    return loans
