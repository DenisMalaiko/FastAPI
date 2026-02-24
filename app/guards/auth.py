import logging
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer(auto_error=False)
logger = logging.getLogger("api-custom")

def get_current_user(credentials: HTTPAuthorizationCredentials | None = Security(security)):
    logger.info("----------")
    if credentials is None:
        raise HTTPException(status_code=401, detail="Missing token")

    token = credentials.credentials

    logger.info(f"GET CURRENT TOKEN - '{token}'")

    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")

    logger.info("User authenticated successfully!")
    logger.info("----------")

    return {"id": 1, "role": "user"}