from fastapi import FastAPI

app = FastAPI(
    title="AI Recruiting Campaign Optimizer",
    description="AI-powered recruiting platform for channel optimization",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "AI Recruiting Campaign Optimizer API Running"}