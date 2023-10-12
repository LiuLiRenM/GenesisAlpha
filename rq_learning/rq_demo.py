import redis
from rq import Queue

from funcs import test_func

pool = redis.ConnectionPool(db=0, host="192.168.31.19", port=6379)
redis_conn = redis.Redis(connection_pool=pool)

if __name__ == "__main__":
    rq_queue = Queue(connection=redis_conn)
    for i in range(10):
        job = rq_queue.enqueue(test_func, "http://www.baidu.com", name=f"{i}")
        print(job)
