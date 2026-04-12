from pydantic import BaseModel, EmailStr
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

    class Config:
        from_attributes = True
