from fastapi import FastAPI
from app.api.users import router as users_router
from app.db.init_db import init_db

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.on_event("startup")
def on_startup():
    init_db()
    print("Database initialized")

# Register routes
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])