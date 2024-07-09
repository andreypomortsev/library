from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.customer import CustomerCreate, CustomerUpdate, Customer
from services import customer_service

router = APIRouter()


@router.post("/users/create", response_model=Customer)
def create_user(user: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_user(user, db)


@router.put("/users/{user_id}/edit", response_model=Customer)
def update_user(user_id: int, user: CustomerUpdate, db: Session = Depends(get_db)):
    return customer_service.update_user(user_id, user, db)


@router.get("/users/{user_id}", response_model=Customer)
def get_author_by_id(user_id: int, db: Session = Depends(get_db)):
    return customer_service.get_user(user_id, db)


@router.get("/users/authors/", response_model=List[Customer])
def get_all_authors(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return customer_service.get_all_users(True, db, skip, limit)


@router.get("/users/", response_model=List[Customer])
def get_all_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return customer_service.get_all_users(False, db, skip, limit)
