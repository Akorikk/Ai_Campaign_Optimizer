from fastapi import APIRouter
import redis
from rq import Queue
from backend.ml.ai_jobs import run_ai_budget

router = APIRouter()

redis_conn = redis.Redis()
queue = Queue("ai_jobs", connection=redis_conn)


@router.post("/run_ai_job")
def run_job(job_title: str, location: str, budget: float):

    job = queue.enqueue(run_ai_budget, job_title, location, budget)

    return {
        "job_id": job.get_id(),
        "status": "queued"
    }