from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.models import Book as DBBook
from schemas.book import Book, BookUpdate, BookCreate


def get_book(book_id: int, db: Session) -> Book:
    db_book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if not db_book:
        msg = f"There is no book with ID: {book_id}"
        raise HTTPException(status_code=404, detail=msg)
    return db_book


def update_book(book_id: int, book_fields: BookUpdate, db: Session) -> Book:
    book = get_book(book_id, db)
    for key, value in book_fields.dict(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session, skip: int = 0, limit: int = 10) -> List[Book]:
    db_books = db.query(DBBook).offset(skip).limit(limit).all()
    if not db_books:
        msg = "There are no books available."
        raise HTTPException(status_code=404, detail=msg)
    return db_books


def create_book(book: BookCreate, db: Session) -> Book:
    db_book = DBBook(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
