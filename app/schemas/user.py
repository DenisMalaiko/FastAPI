from pydantic import BaseModel, ConfigDict

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

    model_config = ConfigDict(from_attributes=True)