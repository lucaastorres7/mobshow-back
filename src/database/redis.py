import redis.asyncio as redis
from config import settings

class RedisClient:
  def __init__(self):
    self._client: redis.Redis | None = None

  async def connect(self):
    self._client = redis.from_url(settings.redis_url, decode_responses=True)
    await self._client.ping()

  async def disconnect(self):
    if self._client:
      await self._client.close()
  
  def get_client(self) -> redis.Redis:
    if not self._client:
      raise RuntimeError("Redis client is not connected")
    return self._client

# Singleton instance of RedisClient
redis_client = RedisClient()