from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.campaign_schema import CampaignCreate
from backend.models.campaign import Campaign
from backend.core.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/campaign")
def create_campaign(data: CampaignCreate, db: Session = Depends(get_db)):

    campaign = Campaign(
        name=data.name,
        job_title=data.job_title,
        location=data.location,
        budget=data.budget
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    return campaign