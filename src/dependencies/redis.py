from database import redis_client
from redis.asyncio import Redis

def get_redis_client() -> Redis:
  return redis_client.get_client()