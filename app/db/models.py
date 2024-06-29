from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, nullable=True)
    birth_year = Column(Integer, nullable=False)
    is_author = Column(Boolean, nullable=False, default=False)

    books = relationship(
        "Book",
        back_populates="author",
        primaryjoin="and_(Customer.id == foreign(Book.author_id), Customer.is_author == True)",
    )


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("customers.id"))
    genre = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    author = relationship("Customer", back_populates="books")
