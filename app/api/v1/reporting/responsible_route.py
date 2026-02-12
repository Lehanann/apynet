from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.repositories.reporting.responsible_repository import ResponsibleRepository
from app.logic.reporting.responsible_service import ResponsibleService
from app.schemas.reporting.responsible_schema import DepartmentResponsibleRead,ServiceResponsibleRead, StructureResponsibleRead

from typing import List

router = APIRouter(prefix="/reporting-responsibles", tags=["reporting-responsibles"])

@router.get("/services",response_model=List[ServiceResponsibleRead])
async def list_service_responsibles(session: AsyncSession = Depends(get_session)):
    repository = ResponsibleRepository(session)
    service = ResponsibleService(repository)
    return await service.list_responsibles_by_service()

@router.get("/departments", response_model=List[DepartmentResponsibleRead])
async def list_department_responsibles(session: AsyncSession = Depends(get_session)):
    repository = ResponsibleRepository(session)
    service = ResponsibleService(repository)
    return await service.list_responsibles_by_department()

@router.get("/structures", response_model=List[StructureResponsibleRead])
async def list_all_responsibles(session: AsyncSession = Depends(get_session)):
    repository = ResponsibleRepository(session)
    service = ResponsibleService(repository)
    return await service.list_all_responsibles()