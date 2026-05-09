import logging
from time import time

from fastapi import APIRouter
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])

_started_at = time()

@router.get("/health")
async def health():
  uptime = round(time() - _started_at)
  return JSONResponse(content={"status": "ok", "uptime": uptime})