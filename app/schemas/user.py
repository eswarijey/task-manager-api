from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str  # plain text, will be hashed before saving


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class Userlogin(BaseModel):
    email: EmailStr
    password: str
