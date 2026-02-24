import time
import uuid
import logging
from fastapi import Request

logger = logging.getLogger("api-custom")

async def logger_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = (time.perf_counter() - start)

    logger.info("-----------")
    logger.info(f"CUSTOM LOGGER {request.method} {request.url.path} - {duration:.4f}s")
    logger.info("-----------")

    return response
