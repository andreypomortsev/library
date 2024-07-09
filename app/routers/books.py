from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.book import BookCreate, Book, BookUpdate
from db.database import get_db
from services import book_service

router = APIRouter()


@router.post("/books/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(book, db)


@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return book_service.update_book(book_id, book, db)


@router.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_book(book_id, db)


@router.get("/books/", response_model=List[Book])
def get_all_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return book_service.get_books(db, skip, limit)
