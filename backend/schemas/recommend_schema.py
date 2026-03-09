from pydantic import BaseModel


class RecommendRequest(BaseModel):
    job_title: str
    location: str