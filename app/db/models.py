from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, nullable=True)
    birth_year = Column(Integer, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))
    genre = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    author = relationship("Author", back_populates="books")
