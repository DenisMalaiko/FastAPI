from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str

class UserUpdate(BaseModel):
    email: str | None = None
    name: str | None = None

class UserOut(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        orm_mode = True
        from_attributes = True