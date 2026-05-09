import logging
import time
from fastapi import Request

logger = logging.getLogger(__name__)

async def logging_middleware(request: Request, call_next):
    start = time.time()
    logger.info(f"→ {request.method} {request.url} - IP: {request.client.host}")
    
    response = await call_next(request)
    
    duration = time.time() - start
    logger.info(f"← {response.status_code} {duration:.3f}s")
    
    return response