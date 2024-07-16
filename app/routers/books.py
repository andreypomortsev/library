from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from schemas.book import BookCreate, Book, BookUpdate
from services import book_service

router = APIRouter()


@router.post("/books/create", response_model=Book)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await book_service.create_book(book, db)


@router.put("/books/{book_id}/edit", response_model=Book)
async def update_book(
    book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db)
):
    return await book_service.update_book(book_id, book, db)


@router.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int, db: AsyncSession = Depends(get_db)):
    return await book_service.get_book(book_id, db)


@router.get("/books/", response_model=List[Book])
async def get_all_books(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    return await book_service.get_books(db, skip, limit)
