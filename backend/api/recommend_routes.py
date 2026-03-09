from fastapi import APIRouter
from backend.schemas.recommend_schema import RecommendRequest
from backend.ml.channel_recommender import recommend_channel

router = APIRouter()


@router.post("/recommend_channel")
def recommend(data: RecommendRequest):

    channel = recommend_channel(
        data.job_title,
        data.location
    )

    return {"recommended_channel": channel}