from pydantic import BaseModel, EmailStr
from uuid import UUID
from app.models.user import UserRole

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None
    password: str
    role: UserRole = UserRole.user

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    phone: str | None
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse