from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.deps import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserCreate, UserUpdate

router = APIRouter()

# Get Users List
@router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)) -> list:
    return db.query(User).all()

# Get User by ID
@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

# Create User
@router.post("/", response_model=UserOut)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    user = User(**payload.model_dump())
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

# Update User
@router.patch("/{id}", response_model=UserOut)
def update_user(
    id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.get(User, id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(user, field, value)

    try:
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.get(User, id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()