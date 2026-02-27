from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    email: str
    name: str

    model_config = ConfigDict(extra="forbid")

class UserUpdate(BaseModel):
    email: str | None = None
    name: str | None = None

    model_config = ConfigDict(extra="forbid")

class UserOut(BaseModel):
    id: int
    email: str
    name: str

    model_config = ConfigDict(from_attributes=True)