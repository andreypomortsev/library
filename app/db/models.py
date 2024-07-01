from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
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

    join = "and_(Customer.id == foreign(Book.author_id), \
        Customer.is_author == True)"
    books = relationship(
        "Book",
        back_populates="author",
        primaryjoin=join,
    )
    loans = relationship("Loan", back_populates="user")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("customers.id"))
    genre = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    author = relationship("Customer", back_populates="books")
    loans = relationship("Loan", back_populates="book")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    loan_date = Column(Date, nullable=False, index=True, default="now()")
    return_date = Column(Date, nullable=True, default=None)

    book = relationship("Book", back_populates="loans")
    user = relationship("Customer", back_populates="loans")
