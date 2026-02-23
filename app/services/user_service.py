from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)

    def create(self, payload: UserCreate) -> User:
        user = User(**payload.model_dump())
        self.db.add(user)

        try:
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise ValueError("Email already exists")

    def update(self, user: User, payload: UserUpdate) -> User:
        data = payload.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(user, field, value)

        try:
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            raise ValueError("Email already exists")

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()