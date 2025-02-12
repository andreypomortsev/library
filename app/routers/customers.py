from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from schemas.customer import CustomerCreate, CustomerUpdate, Customer
from services import customer_service

router = APIRouter()


@router.post("/users", response_model=Customer)
async def create_user(user: CustomerCreate, db: AsyncSession = Depends(get_db)):
    return await customer_service.create_user(user, db)


@router.get("/users/{user_id}", response_model=Customer)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await customer_service.get_user(user_id, db)


@router.get("/users/", response_model=List[Customer])
async def get_all_authors(
    skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_db)
):
    return await customer_service.get_all_users(True, db, skip, limit)


@router.get("/users", response_model=List[Customer])
async def get_all_users(
    skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_db)
):
    return await customer_service.get_all_users(False, db, skip, limit)


@router.put("/users/{user_id}", response_model=Customer)
async def update_user(
    user_id: int, user: CustomerUpdate, db: AsyncSession = Depends(get_db)
):
    return await customer_service.update_user(user_id, user, db)
