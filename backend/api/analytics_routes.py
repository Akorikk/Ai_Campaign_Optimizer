from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import SessionLocal
from backend.models.campaign import Campaign
from sqlalchemy import func

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/campaign_analytics")
def analytics(db: Session = Depends(get_db)):

    total_campaigns = db.query(func.count(Campaign.id)).scalar()

    total_budget = db.query(func.sum(Campaign.budget)).scalar() or 0

    avg_budget = db.query(func.avg(Campaign.budget)).scalar() or 0

    return {
        "total_campaigns": total_campaigns,
        "total_budget": round(total_budget,2),
        "average_budget": round(avg_budget,2)
    }