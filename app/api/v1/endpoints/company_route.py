from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.services.company_service import CompanyService
from app.schemas.company_schema import CompanyCreate, CompanyRead, CompanyUpdate

router = APIRouter(prefix="/companies", tags=["companies"])

@router.get("/",response_model=list[CompanyRead])
async def list_companies(db: AsyncSession = Depends(get_session)):
    service = CompanyService(db)
    try:
        return await service.list_companies()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{company_id}", response_model=CompanyRead)
async def get_company(company_id: int, db: AsyncSession = Depends(get_session)):
    service = CompanyService(db)
    try:
        return await service.get_company(company_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/company/{company_name}", response_model=CompanyRead)
async def get_company_by_name(company_name: str, db: AsyncSession = Depends(get_session)):
    service = CompanyService(db)
    return await service.get_company_by_name(company_name)

@router.post("/", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
async def create_company(data: CompanyCreate, db: AsyncSession = Depends(get_session)):
    service = CompanyService(db)
    try:
        return await service.create_company(data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put("/{company_id}", response_model=CompanyRead)
@router.patch("/{company_id}", response_model=CompanyRead)
async def update_company(company_id: int, data: CompanyUpdate, db: AsyncSession = Depends(get_session)):
    service = CompanyService(db)
    try:
        return await service.update_company(company_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(company_id: int, db: AsyncSession = Depends(get_session)):
    service = CompanyService(db)
    try:
        return await service.delete_company(company_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))