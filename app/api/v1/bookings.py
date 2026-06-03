from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.booking import Booking
from app.models.service import Service
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingResponse, BookingStatusUpdate
from app.api.deps import get_current_user
from typing import List

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingResponse, status_code=201)
async def create_booking(
    data: BookingCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Service).where(Service.id == data.service_id))
    service = result.scalar_one_or_none()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    booking = Booking(
        user_id=current_user.id,
        service_id=data.service_id,
        scheduled_at=data.scheduled_at,
        address=data.address,
        total_amount=service.price
    )
    db.add(booking)
    await db.commit()
    await db.refresh(booking)
    return booking

@router.get("/my", response_model=List[BookingResponse])
async def my_bookings(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Booking).where(Booking.user_id == current_user.id)
    )
    return result.scalars().all()

@router.patch("/{booking_id}/status", response_model=BookingResponse)
async def update_status(
    booking_id: str,
    data: BookingStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    booking = result.scalar_one_or_none()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.status = data.status
    await db.commit()
    await db.refresh(booking)
    return booking