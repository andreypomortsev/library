from core.database import Base
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(
        Integer, ForeignKey("books.id"), index=True, nullable=False
    )
    user_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    loan_date = Column(Date, nullable=False, index=True, default="now()")
    return_date = Column(Date, nullable=True, default=None)

    book = relationship("Book", back_populates="loans", lazy="selectin")
    user = relationship("Customer", back_populates="loans", lazy="selectin")
