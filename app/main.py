from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import engine, Base
from app.api.v1 import auth, services, bookings
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Household Services Platform API",
    lifespan=lifespan
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(services.router, prefix="/api/v1")
app.include_router(bookings.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "project": "Resido – Household Services API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }