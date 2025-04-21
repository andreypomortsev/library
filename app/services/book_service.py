from typing import List

from models.book import Book as DBBook
from fastapi import HTTPException
from schemas.book import Book, BookCreate, BookUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_book(book_id: int, db: AsyncSession) -> Book:
    query = select(DBBook).filter(DBBook.id == book_id)
    result = await db.execute(query)
    db_book = result.scalars().first()
    if not db_book:
        msg = f"There is no book with ID: {book_id}"
        raise HTTPException(status_code=404, detail=msg)
    return db_book


async def update_book(
    book_id: int, book_fields: BookUpdate, db: AsyncSession
) -> Book:
    book = await get_book(book_id, db)
    for key, value in book_fields.model_dump(exclude_unset=True).items():
        setattr(book, key, value)
    await db.commit()
    await db.refresh(book)
    return book


async def get_books(
    db: AsyncSession, skip: int = 0, limit: int = 10
) -> List[Book]:
    result = await db.execute(select(DBBook).offset(skip).limit(limit))
    db_books = result.scalars().all()
    if not db_books:
        msg = "There are no books available."
        raise HTTPException(status_code=404, detail=msg)
    return db_books


async def create_book(book: BookCreate, db: AsyncSession) -> Book:
    db_book = DBBook(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book
