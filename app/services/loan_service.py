from typing import List, Optional

from models.loan import Loan as DBLoan
from fastapi import HTTPException
from schemas.loan import Loan, LoanCreate, LoanUpdate
from sqlalchemy import Date, select, text
from sqlalchemy.ext.asyncio import AsyncSession


async def create_loan(loan: LoanCreate, db: AsyncSession) -> Loan:
    query = text("SELECT create_book_loan(:book_id, :user_id, :loan_date)")
    await db.execute(
        query,
        {
            "book_id": loan.book_id,
            "user_id": loan.user_id,
            "loan_date": loan.loan_date,
        },
    )
    await db.commit()

    return await get_loan(loan.book_id, db, None)


async def get_loan(
    book_id: int, db: AsyncSession, return_date: Optional[Date]
) -> Loan:
    query = (
        select(DBLoan)
        .filter(DBLoan.book_id == book_id, DBLoan.return_date == return_date)
        .order_by(DBLoan.id.desc())
    )
    result = await db.execute(query)
    db_loan = result.scalars().first()
    if not db_loan:
        msg = f"There is no loan with ID: {book_id}"
        raise HTTPException(status_code=404, detail=msg)

    return db_loan


async def get_loans(db: AsyncSession, skip: int, limit: int) -> List[Loan]:
    result = await db.execute(select(DBLoan).offset(skip).limit(limit))
    db_loans = result.scalars().all()
    if not db_loans:
        msg = "There are no loans yet."
        raise HTTPException(status_code=404, detail=msg)

    return db_loans


async def update_loan(
    book_id: int, loan: LoanUpdate, db: AsyncSession
) -> Loan:
    close_query = text("SELECT return_book(:book_id, :return_date)")
    params = {"book_id": book_id, "return_date": loan.return_date}
    await db.execute(close_query, params)
    await db.commit()

    return await get_loan(book_id, db, loan.return_date)
