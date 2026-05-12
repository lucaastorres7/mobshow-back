# GENERAL LIBS
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI

# CUSTOM LIBS
from config import settings
from middlewares import logging_middleware
from database import redis_client
from routers import health_router

# --- LOGGING ---
logging.basicConfig(
  level=settings.log_level.upper(),
  format="[%(asctime)s] - [%(levelname)s] %(name)s — %(message)s",
)
logger = logging.getLogger(__name__)

# --- LIFECYCLE ---
@asynccontextmanager
async def lifespan(app: FastAPI):
  logger.info("Starting Mobshow API...")
  await redis_client.connect()
  logger.info("Connected to Redis successfully.")
  yield
  await redis_client.disconnect()
  logger.info("Disconnected from Redis successfully.")
  logger.info("Shutting down Mobshow API...")

app = FastAPI(
  title="Mobshow API",
  version="1.0.0",
  docs_url="/docs",
  lifespan=lifespan
)

# --- MIDDLEWARES ---
app.middleware("http")(logging_middleware)

# --- ROUTES ---
app.include_router(health_router)