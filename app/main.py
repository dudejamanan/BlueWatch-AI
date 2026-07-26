from fastapi import FastAPI
from app.core.logging import logger

from app.core.config import settings
from app.api.routes.root import router as root_router
from app.api.routes.health import router as health_router

app = FastAPI(
    title=settings.project_name,
    version=settings.api_version,
)
logger.info("BlueWatch API started successfully.")

app.include_router(root_router)
app.include_router(health_router)