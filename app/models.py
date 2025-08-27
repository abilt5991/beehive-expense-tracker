from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base
from uuid import uuid4

def generate_uuid():
    return str(uuid4())

class Expense(Base):
    __tablename__="expenses"
    __table_args__ = {'extend_existing': True}

    expenseID = Column("expenseID", String, primary_key=True, default=generate_uuid)
    expenseName = Column("expenseName", String, nullable=False)
    date = Column("date", Date, nullable=False)
    category = Column("category", String, nullable=False)
    amount = Column("amount", Float, nullable=False)


    def __init__(self, expenseName, date, category, amount):
        self.expenseName = expenseName
        self.date = date
        self.category = category
        self.amount = amount


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    limit_amount = Column(Float, default=0, nullable=False)