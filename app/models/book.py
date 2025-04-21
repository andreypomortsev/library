from core.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("customers.id"))
    genre = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    author = relationship("Customer", back_populates="books", lazy="selectin")
    loans = relationship("Loan", back_populates="book", lazy="selectin")
