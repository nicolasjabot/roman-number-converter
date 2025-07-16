import redis
import os
import sys

def connect_redis():
    url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    try:
        # client = redis.Redis.from_url(url, decode_responses=True)
        client = redis.Redis(host="redis-server")
        client.ping()
        return client
    except redis.exceptions.RedisError as exc:
        print(f"WARNING: Redis unavailable ({exc}); cache disabled", file=sys.stderr)
        return None