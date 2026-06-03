from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.service import Service
from app.models.user import User
from app.schemas.service import ServiceCreate, ServiceResponse
from app.api.deps import get_current_user
from typing import List

router = APIRouter(prefix="/services", tags=["Services"])

@router.get("/", response_model=List[ServiceResponse])
async def get_services(
    category: str | None = Query(None),
    db: AsyncSession = Depends(get_db)
):
    query = select(Service).where(Service.available == True)
    if category:
        query = query.where(Service.category == category)
    result = await db.execute(query)
    return result.scalars().all()

@router.post("/", response_model=ServiceResponse, status_code=201)
async def create_service(
    data: ServiceCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = Service(**data.model_dump())
    db.add(service)
    await db.commit()
    await db.refresh(service)
    return service