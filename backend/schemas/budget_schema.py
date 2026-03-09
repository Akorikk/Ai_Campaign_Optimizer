from pydantic import BaseModel

class BudgetRequest(BaseModel):
    job_title: str
    location: str
    budget: float