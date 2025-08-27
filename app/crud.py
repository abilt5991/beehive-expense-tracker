from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import func
from datetime import datetime
from calendar import monthrange

def seed_categories(db: Session):
    categories = [
        {"name": "Groceries", "limit_amount": 600},
        {"name": "Bills", "limit_amount": 600},
        {"name": "Takeaway", "limit_amount": 200},
        {"name": "Personal", "limit_amount":200},
        {"name": "Pet", "limit_amount": 300}
    ]
    for category in categories:
        db.add(models.Category(**category))
    db.commit()

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expense(db:Session, skip: int=0, limit: int = 100):
    return db.query(models.Expense).offset(skip).limit(limit).all()

def remove_expense(db: Session, expense_id: str):
    expense = db.query(models.Expense).filter(models.Expense.expenseID == expense_id).first()
    if not expense:
        return False
    db.delete(expense)
    db.commit()
    return True

def update_expense(db: Session, expense_id: str, updated: schemas.ExpenseCreate):
    expense = db.query(models.Expense).filter(models.Expense.expenseID == expense_id).first()
    if not expense:
        return None
    expense.expenseName = updated.expenseName
    expense.amount = updated.amount
    expense.date = updated.date
    expense.category = updated.category
    db.commit()
    db.refresh(expense)
    return expense

def get_summary(db:Session, year: int, month: int):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month, monthrange(year, month)[1])
    category_spent = (db.query(models.Expense.category, func.sum(models.Expense.amount))
                       .filter(models.Expense.date.between(start_date, end_date))
                       .group_by(models.Expense.category)
                       .all())

    category_spent = {category: float(total) for category, total in category_spent}
    print(category_spent)

    categories = db.query(models.Category).all()
    breakdown = {}
    for category in categories:
        spent = category_spent.get(category.name, 0)
        breakdown[category.name] = {
            "spent": spent,
            "limit": category.limit_amount,
            "overspent": spent > category.limit_amount
        }
    monthly_total = sum(item["spent"] for item in breakdown.values())

    return breakdown, monthly_total