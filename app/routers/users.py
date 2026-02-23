from fastapi import APIRouter, Depends, HTTPException

from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.services.user_service import UserService
from app.services.deps import get_user_service


router = APIRouter()

# Get Users List
@router.get("/", response_model=list[UserOut])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_all()

# Get User by ID
@router.get("/{id}", response_model=UserOut)
def get_user(id: int, service: UserService = Depends(get_user_service)):
    user = service.get_by_id(id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# Create User
@router.post("/", response_model=UserOut)
def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return service.create(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Update User
@router.patch("/{id}", response_model=UserOut)
def update_user(
    id: int,
    payload: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    user = service.get_by_id(id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        return service.update(user, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{id}", status_code=204)
def delete_user(id: int, service: UserService = Depends(get_user_service)):
    user = service.get_by_id(id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    service.delete(user)