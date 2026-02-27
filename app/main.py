import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends

from app.routers.users import router as users_router
from app.db.init_db import init_db
from app.middleware.logger import logger_middleware
from app.guards.auth import auth_guard

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

api_logger = logging.getLogger("api-custom")
api_logger.setLevel(logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("Database initialized")
    yield

app = FastAPI(title="My API", version="1.0.0", lifespan=lifespan)
app.middleware("http")(logger_middleware)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/me")
def me(user = Depends(auth_guard)):
    return user

# Register routes
app.include_router(
    users_router,
    prefix="/api/v1/users",
    tags=["users"],
    dependencies=[Depends(auth_guard)]
)