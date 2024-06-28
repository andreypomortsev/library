from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, nullable=True)
    birth_year = Column(Integer)
