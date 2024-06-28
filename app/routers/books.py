from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.book import BookCreate, BookUpdate, Book
from db.models import Book as DBBook
from db.database import get_db, get_author_id_by_name_last_name

router = APIRouter()


@router.post("/books/create", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Получение ID автора используя storing procedure
    author_id = get_author_id_by_name_last_name(
       db, book.author_name, book.author_last_name, book.author_birth_year
    )
    if not author_id:
        raise HTTPException(status_code=404, detail="Автор не найден")

    # Создаем книгу с полученным ID автора
    db_book = DBBook(
        title=book.title, author_id=author_id, year=book.year
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.put("/books/{book_id}/edit", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("/books/{book_id}", response_model=Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Не удалось найти книгу с таким id")
    return db_book
