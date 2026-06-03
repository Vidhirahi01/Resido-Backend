from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.models.booking import BookingStatus

class BookingCreate(BaseModel):
    service_id: UUID
    scheduled_at: datetime
    address: str

class BookingStatusUpdate(BaseModel):
    status: BookingStatus

class BookingResponse(BaseModel):
    id: UUID
    user_id: UUID
    service_id: UUID
    status: BookingStatus
    scheduled_at: datetime
    address: str
    total_amount: float | None
    created_at: datetime

    class Config:
        from_attributes = True