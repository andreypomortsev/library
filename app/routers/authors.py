from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.author import AuthorCreate, AuthorUpdate, Author
from db.models import Author as DBAuthor
from db.database import get_db

router = APIRouter()


@router.post("/authors/create", response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = DBAuthor(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@router.put("/authors/{author_id}/edit", response_model=Author)
def update_author(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    db_author = db.query(DBAuthor).filter(DBAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    for key, value in author.dict(exclude_unset=True).items():
        setattr(db_author, key, value)
    db.commit()
    db.refresh(db_author)
    return db_author


@router.get("/authors/{author_id}", response_model=Author)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(DBAuthor).filter(DBAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Не удалось найти автора с таким id")
    return db_author
