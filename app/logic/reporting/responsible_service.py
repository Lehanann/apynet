from typing import List
from app.repositories.reporting.responsible_repository import ResponsibleRepository
from app.schemas.reporting.responsible_schema import DepartmentResponsibleRead, ServiceResponsibleRead, StructureResponsibleRead
from fastapi import HTTPException, status

class ResponsibleService:
    def __init__(self, repository: ResponsibleRepository):
        self.repository = repository

    async def list_responsibles_by_department(self) -> List[DepartmentResponsibleRead]:
        items = await self.repository.get_all_departments()
        if not items:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found")
        return items

    async def list_responsibles_by_service(self) -> List[ServiceResponsibleRead]:
        items = await self.repository.get_all_services()
        if not items:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found")
        return items
    
    async def list_all_responsibles(self) -> List[StructureResponsibleRead]:
        items = await self.repository.get_all_structures()
        if not items:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found")
        return items