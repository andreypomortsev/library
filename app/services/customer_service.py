from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.models import Customer as DBCustomer
from schemas.customer import Customer, CustomerUpdate, CustomerCreate


def create_user(user: CustomerCreate, db: Session) -> Customer:
    db_customer = DBCustomer(**user.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_user(user_id: int, db: Session) -> Customer:
    db_customer = db.query(DBCustomer).filter(DBCustomer.id == user_id).first()
    if not db_customer:
        msg = f"There is no user with ID: {user_id}"
        raise HTTPException(status_code=404, detail=msg)
    return db_customer


def update_user(user_id: int, user: CustomerUpdate, db: Session) -> Customer:
    db_customer = get_user(user_id, db)
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_all_users(
    authors: bool, db: Session, skip: int = 0, limit: int = 50
) -> List[Customer]:
    db_authors = (
        db.query(DBCustomer)
        .filter(DBCustomer.is_author == authors)
        .offset(skip)
        .limit(limit)
        .all()
    )
    if not db_authors:
        msg = f"There are no authors here."
        raise HTTPException(status_code=404, detail=msg)
    return db_authors
