import redis
from rq import Worker, Queue, Connection

listen = ["ai_jobs"]

redis_conn = redis.Redis(host="localhost", port=6379)

with Connection(redis_conn):
    worker = Worker(listen)
    worker.work()