from fastapi import FastAPI, Response, Depends
from sqlalchemy.orm import Session
from app import database, schemas, crud, models

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

def seed_categories_once():
    db = database.SessionLocal()
    if not db.query(models.Category).first():  # only seed if empty
        crud.seed_categories(db)
    db.close()
seed_categories_once()

@app.post("/expenses/", response_model=schemas.ExpenseOut)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

@app.get("/expenses/", response_model=list[schemas.ExpenseOut])
def list_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_expense(db, skip=skip, limit=limit)

@app.put("/expenses/{expense_id}", response_model=schemas.ExpenseOut)
def edit_expense(expense_id: str, updated: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    expense = crud.update_expense(db, expense_id, updated)
    if not expense:
        return {"error": f"Expense {expense_id} not found"}
    return expense

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: str, db: Session = Depends(get_db)):
    success = crud.remove_expense(db, expense_id)
    if success:
        return {"message": f"Expense {expense_id} deleted successfully"}
    else:
        return {"error": f"Expense {expense_id} not found"}

@app.get("/summary/{year}/{month}")
def full_summary(year: int, month: int, db: Session = Depends(get_db)):
    category_totals, monthly_total = crud.get_summary(db, year, month)
    monthly_budget = sum(cat["limit"] for cat in category_totals.values())
    remaining_budget = monthly_budget - monthly_total
    return {
        "year": year,
        "month": month,
        "total_spent": monthly_total,
        "remaining_budget": remaining_budget,
        "budget": monthly_budget,
        "categories": category_totals
    }

