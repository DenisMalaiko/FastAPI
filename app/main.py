import logging
from fastapi import FastAPI, Depends
from app.routers.users import router as users_router
from app.db.init_db import init_db
from app.middleware.logger import logger_middleware
from app.guards.auth import get_current_user

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

api_logger = logging.getLogger("api-custom")
api_logger.setLevel(logging.INFO)

app = FastAPI(title="My API", version="1.0.0")
app.middleware("http")(logger_middleware)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/me")
def me(user = Depends(get_current_user)):
    return user

@app.on_event("startup")
def on_startup():
    init_db()
    print("Database initialized")

# Register routes
app.include_router(
    users_router,
    prefix="/api/v1/users",
    tags=["users"],
    dependencies=[Depends(get_current_user)]
)