from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.customer import CustomerCreate, CustomerUpdate, Customer
from db.models import Customer as DBCustomer
from db.database import get_db

router = APIRouter()


@router.post("/user/create", response_model=Customer)
def create_user(user: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = DBCustomer(**user.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.put("/user/{user_id}/edit", response_model=Customer)
def update_user(user_id: int, user: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(DBCustomer).filter(DBCustomer.id == user_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@router.get("/user/{user_id}", response_model=Customer)
def get_author_by_id(user_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(DBCustomer).filter(DBCustomer.id == user_id).first()
    if not db_customer:
        raise HTTPException(
            status_code=404, detail="Не удалось найти пользователя с таким id"
        )
    return db_customer


@router.get("/users/", response_model=List[Customer])
def get_all_authors(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    authors = (
        db.query(DBCustomer)
        .filter(DBCustomer.is_author)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return authors
