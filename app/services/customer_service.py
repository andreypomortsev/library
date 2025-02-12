from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Customer as DBCustomer
from schemas.customer import Customer, CustomerUpdate, CustomerCreate


async def create_user(user: CustomerCreate, db: AsyncSession) -> Customer:
    db_customer = DBCustomer(**user.model_dump())
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer


async def get_user(user_id: int, db: AsyncSession) -> Customer:
    query = select(DBCustomer).filter(DBCustomer.id == user_id)
    result = await db.execute(query)
    db_customer = result.scalars().first()
    if not db_customer:
        msg = f"There is no user with ID: {user_id}"
        raise HTTPException(status_code=404, detail=msg)
    return db_customer


async def update_user(
    user_id: int, user: CustomerUpdate, db: AsyncSession
) -> Customer:
    db_customer = await get_user(user_id, db)
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_customer, key, value)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer


async def get_all_users(
    authors: bool, db: AsyncSession, skip: int = 0, limit: int = 50
) -> List[Customer]:
    query = (
        select(DBCustomer)
        .filter(DBCustomer.is_author == authors)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(query)
    db_authors = result.scalars().all()
    if not db_authors:
        msg = "There are no authors here."
        raise HTTPException(status_code=404, detail=msg)
    return db_authors
