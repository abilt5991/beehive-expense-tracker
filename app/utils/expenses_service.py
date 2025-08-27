from app.config import CATEGORY_LIMITS, MONTHLY_LIMIT
from app import crud
from sqlalchemy.orm import Session

def check_limits(db: Session):
    category_totals, monthly_total = crud.get_totals(db)

    return {
        "category_totals" : category_totals,
        "monthly_total" : monthly_total,
        "category_status" : {
            category : ("OK" if category_totals.get(category, 0) <= limit else "Over Limit") for category, limit in CATEGORY_LIMITS.items()
        },
        "monthly_status" : ("OK" if monthly_total <= MONTHLY_LIMIT else "Over Limit")
    }
