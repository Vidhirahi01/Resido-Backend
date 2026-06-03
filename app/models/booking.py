from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum
from datetime import datetime
from app.core.database import Base

class BookingStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)
    provider_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    status = Column(Enum(BookingStatus), default=BookingStatus.pending)
    scheduled_at = Column(DateTime, nullable=False)
    address = Column(String, nullable=False)
    total_amount = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="bookings", foreign_keys=[user_id])
    service = relationship("Service", back_populates="bookings")