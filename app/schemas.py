from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    expenseName: str
    date: date
    category: str
    amount: float

class ExpenseOut(ExpenseCreate):
    expenseID: str

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    limit_amount: float

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
    class Config:
        from_attributes = True