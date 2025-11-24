from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings
from collections.abc import AsyncGenerator

# creation du moteur asynchrone
engine = create_async_engine(
    settings.dsn_async,
    echo=True,
    future=True
)

Base = declarative_base(metadata=MetaData(schema=settings.PG_SCHEMA))

# Fabrique de sessions asynchrones
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dépendance pratique (ex: pour FastAPI)
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session