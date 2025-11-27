from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.department_service import DepartmentService
from app.schemas.department_schema import DepartmentCreate, DepartmentRead, DepartmentUpdate

router = APIRouter(prefix="/departments", tags=["departments"])

@router.get("/", response_model=list[DepartmentRead])
async def list_departments(db: AsyncSession = Depends(get_session)):
    service = DepartmentService(db)
    try:
        return await service.list_departments()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{department_id}", response_model=DepartmentRead)
async def get_department(department_id: int, db: AsyncSession = Depends(get_session)):
    service = DepartmentService(db)
    try:
        return await service.get_department(department_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/", response_model=DepartmentRead, status_code=status.HTTP_201_CREATED)
async def create_company(data: DepartmentCreate, db: AsyncSession = Depends(get_session)):
    service = DepartmentService(db)
    try:
        return await service.create_department(data)
    except ValueError as e:
         raise HTTPException(status_code=404, detail=str(e))

@router.put("/{department_id}", response_model=DepartmentRead)
@router.patch("/{department_id}", response_model=DepartmentRead)
async def update_department(department_id: int, data: DepartmentUpdate, db: AsyncSession = Depends(get_session)):
    service = DepartmentService(db)
    try:
        return await service.update_department(department_id,data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(department_id: int, db: AsyncSession = Depends(get_session)):
    service = DepartmentService(db)
    try:
        return await service.delete_department(department_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))