from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.service_repository import ServiceRepository
from app.schemas.service_schema import ServiceCreate, ServiceUpdate

class ServiceManager:
    def __init__(self, db: AsyncSession):
        self.repository = ServiceRepository(db)

    async def list_services(self):
        return await self.repository.get_all()
    
    async def get_service(self, service_id: int):
        service = await self.repository.get_by_id(service_id)
        if not service:
            raise ValueError("service not found")
        return service

    async def create_service(self, data: ServiceCreate):
        if await self.repository.get_by_id(data.name):
            raise ValueError(f"the service name: {data.name} already exists!")
        return await self.repository.create(data)
    
    async def update_service(self, service_id, data: ServiceUpdate):
        service = await self.repository.get_by_id(service_id)
        if not service:
            raise ValueError("service not found!")
        
        if data.name and data.name != service.name:
            if await self.repository.get_by_name(data.name):
                raise ValueError(f"the service name: {data.name} already exists!")
        return await self.repository.update(service_id, data)
    
    async def delete_service(self, service_id: int):
        service = await self.repository.get_by_id(service_id)
        if not service:
            raise ValueError("service not found")
        return {"message": "service successfully deleted"}
    