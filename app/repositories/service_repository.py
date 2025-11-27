from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.service import Service
from app.schemas.service_schema import ServiceCreate, ServiceUpdate

class ServiceRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, service_id: int):
        request = await self.db.execute(select(Service).where(Service.id_service == service_id))
        return request.scalars().first()

    async def get_by_name(self, service_name: str):
        request = await self.db.execute(select(Service).where(Service.name == service_name))
        return request.scalars().first()

    async def get_all(self):
        request = await self.db.execute(select(Service))
        return request.scalars().all()

    async def create(self, data: ServiceCreate):
        service = Service(**data.model_dump())
        self.db.add(service)
        await self.db.commit()
        await self.db.refresh(service)
        return service

    async def update(self, service_id: int, data: ServiceUpdate):
        service = await self.get_by_id(service_id)
        if not service:
            return None
        
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(service, key, value)
        
        await self.db.commit()
        await self.db.refresh(service)
        return service

    async def delete(self, service_id: int):
        service = await self.get_by_id(service_id)
        if not service:
            return False
        await self.db.delete(service)
        await self.db.commit()
        return True