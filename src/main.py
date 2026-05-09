from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI

from log import configure_logging
from config import settings

configure_logging(settings.log_level)

logger = logging.getLogger(__name__)

# --- LIFECYCLE ---
@asynccontextmanager
async def lifespan(app: FastAPI):
  logger.info("Starting Mobshow API...")
  yield
  logger.info("Shutting down Mobshow API...")

app = FastAPI(
  title="Mobshow API",
  version="1.0.0",
  docs_url="/docs",
  lifespan=lifespan
)
