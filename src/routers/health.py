import logging
from time import time
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from redis.asyncio import Redis
from dependencies import get_redis_client

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

_started_at = time()

@router.get("/health")
async def health(redis: Redis = Depends(get_redis_client)):
  uptime = round(time() - _started_at)

  try:
    await redis.ping()
    redis_status = "connected"
    server_status = "healthy"
    status = 200

  except Exception:
    redis_status = "unavailable"
    server_status = "unhealthy"
    status = 503

  return JSONResponse(
    status_code=status,
    content={
      "status": server_status,
      "uptime_seconds": uptime,
      "redis": redis_status
    }
  )