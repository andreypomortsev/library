from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import text, Date
from sqlalchemy.orm import Session

from db.models import Loan as DBLoan
from schemas.loan import Loan, LoanUpdate, LoanCreate


def create_loan(loan: LoanCreate, db: Session) -> Loan:
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

    return get_loan(loan.book_id, db, None)


def get_loan(book_id: int, db: Session, return_date: Optional[Date]) -> Loan:
    db_loan = (
        db.query(DBLoan)
        .filter(DBLoan.book_id == book_id, DBLoan.return_date == return_date)
        .order_by(DBLoan.id.desc())
        .first()
    )
    if not db_loan:
        msg = f"There is no loan with ID: {book_id}"
        raise HTTPException(status_code=404, detail=msg)

    return db_loan


def get_loans(db: Session, skip: int, limit: int) -> List[Loan]:
    db_loans = db.query(DBLoan).offset(skip).limit(limit).all()
    if not db_loans:
        msg = "There are no loans yet."
        raise HTTPException(status_code=404, detail=msg)

    return db_loans


def update_loan(book_id: int, loan: LoanUpdate, db: Session) -> Loan:
    close_query = text("SELECT return_book(:book_id, :return_date)")
    params = {"book_id": book_id, "return_date": loan.return_date}
    db.execute(close_query, params)
    db.commit()

    return get_loan(book_id, db, loan.return_date)
