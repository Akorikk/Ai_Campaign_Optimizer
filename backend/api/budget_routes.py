from fastapi import APIRouter
from backend.schemas.budget_schema import BudgetRequest
from backend.ml.channel_recommender import recommend_channel
from backend.ml.budget_allocator import allocate_budget

router = APIRouter()

@router.post("/allocate_budget")
def allocate(data: BudgetRequest):

    channel = recommend_channel(data.job_title, data.location)

    allocation = allocate_budget(channel, data.budget)

    return {
        "recommended_primary_channel": channel,
        "budget_allocation": allocation
    }