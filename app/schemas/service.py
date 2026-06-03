from pydantic import BaseModel
from uuid import UUID

class ServiceCreate(BaseModel):
    name: str
    category: str
    description: str | None = None
    price: float

class ServiceResponse(BaseModel):
    id: UUID
    name: str
    category: str
    description: str | None
    price: float
    available: bool

    class Config:
        from_attributes = True