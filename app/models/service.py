from sqlalchemy import Column, String, Float, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    available = Column(Boolean, default=True)

    bookings = relationship("Booking", back_populates="service")