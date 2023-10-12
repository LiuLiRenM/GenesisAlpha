import redis
from rq import Connection, Worker, Queue

listen = ["high", "default", "low"]

pool = redis.ConnectionPool(host="192.168.31.19", port=6379, db=0)
redis_conn = redis.Redis(connection_pool=pool)


if __name__ == "__main__":
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()
