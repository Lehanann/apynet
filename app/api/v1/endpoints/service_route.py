from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.service_manager import ServiceManager
from app.schemas.service_schema import ServiceCreate, ServiceRead, ServiceUpdate


router = APIRouter(prefix="/services", tags=["services"])

@router.get("/", response_model=list[ServiceRead])
async def list_services(db: AsyncSession = Depends(get_session)):
    service = ServiceManager(db)
    try:
        return await service.list_services()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{service_id}", response_model=ServiceRead)
async def get_service(service_id: int, db: AsyncSession = Depends(get_session)):
    service = ServiceManager(db)
    try:
        return await service.get_service(service_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/", response_model=ServiceRead, status_code=status.HTTP_201_CREATED)
async def create_company(data: ServiceCreate, db: AsyncSession = Depends(get_session)):
    service = ServiceManager(db)
    try:
        return await service.create_service(data)
    except ValueError as e:
         raise HTTPException(status_code=404, detail=str(e))

@router.put("/{service_id}", response_model=ServiceRead)
@router.patch("/{service_id}", response_model=ServiceRead)
async def update_service(service_id: int, data: ServiceUpdate, db: AsyncSession = Depends(get_session)):
    service = ServiceManager(db)
    try:
        return await service.update_service(service_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service(service_id: int, db: AsyncSession = Depends(get_session)):
    service = ServiceManager(db)
    try:
        return await service.delete_service(service_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))