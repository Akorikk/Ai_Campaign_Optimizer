from fastapi import FastAPI
from backend.core.database import engine, Base
from backend.models import campaign
from backend.api import campaign_routes
from backend.api import recommend_routes
from backend.api import budget_routes
# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Recruiting Campaign Optimizer"
)

# register API routes
app.include_router(campaign_routes.router)
app.include_router(budget_routes.router)
app.include_router(recommend_routes.router)

@app.get("/")
def home():
    return {"message": "AI Recruiting Campaign Optimizer API Running"}