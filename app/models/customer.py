from core.database import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, nullable=True)
    birth_year = Column(Integer, nullable=False)
    is_author = Column(Boolean, nullable=False, default=False)

    books = relationship("Book", back_populates="author", lazy="selectin")
    loans = relationship("Loan", back_populates="user", lazy="selectin")
