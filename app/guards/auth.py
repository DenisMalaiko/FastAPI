import logging
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer(auto_error=False)
logger = logging.getLogger("api-custom")

def get_current_user(credentials: HTTPAuthorizationCredentials | None = Security(security)):
    if credentials is None:
        raise HTTPException(status_code=401, detail="Missing token")

    token = credentials.credentials

    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": "Successfully authenticated!"}