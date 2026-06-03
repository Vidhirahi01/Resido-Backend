from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import enum
from app.core.database import Base

class UserRole(str, enum.Enum):
    user = "user"
    provider = "provider"
    admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user, nullable=False)
    is_active = Column(Boolean, default=True)
    address = Column(String, nullable=True)

    bookings = relationship("Booking", back_populates="user", foreign_keys="Booking.user_id")