from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.company_service import CompanyService
from app.schemas.company_schema import CompanyCreate, CompanyRead, CompanyUpdate
from app.repositories.company_repository import CompanyRepository

router = APIRouter(prefix="/companies", tags=["companies"])

def get_company_service(db: AsyncSession = Depends(get_session)) -> CompanyService:
    return CompanyService(CompanyRepository(db), db)

@router.get("/",response_model=list[CompanyRead])
async def list_companies(service: CompanyService = Depends(get_company_service)):
    """
    Retrieve a list of all companies from the database.

    This endpoint fetches all companies stored in the database and returns 
    them in the format specified by the `CompanyRead` schema.

    Args:
        service (CompanyService, optional): The service layer for handling
            company-related operations. This is injected automatically using
            `Depends(get_company_service)`.

    Returns:
        List[CompanyRead]: A list of companies represented by the `CompanyRead`
            schema, which includes relevant company details such as name and ID.
    """
    return await service.get_all()

@router.get("/{company_id}", response_model=CompanyRead)
async def get_company(company_id: int, service: CompanyService = Depends(get_company_service)) -> CompanyRead:
    """
    Retrieve company by its ID from the database.

    This endpoint fetches a company by its ID stored in the database and returns 
    them in the format specified by the `CompanyRead` schema.

    Args:
        company_id (int): Unique identifier of th ecompany
        Args:
        service (CompanyService, optional): The service layer for handling
            company-related operations. This is injected automatically using
            `Depends(get_company_service)`.

    Returns:
        company (CompanyRead): A company represented by the `CompanyRead`
            schema, which includes relevant company details such as name and ID.
    """
    
    return await service.get_by_id(company_id)
    
"""@router.get("/company/{company_name}", response_model=CompanyRead)
async def get_company_by_name(company_name: str, service: CompanyService = Depends(get_company_service)):
    service = CompanyService(db)
    return await service.get_company_by_name(company_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_company(data: CompanyCreate, service: CompanyService = Depends(get_company_service)) -> dict[str,str]:
    """
    Create a new company.

    Args:
        data (CompanyCreate): The datas used to create the company.
        service (CompanyService, optional): The service layer for handling
            company-related operations. This is injected automatically using
            `Depends(get_company_service)`.

    Raises:
        HTTPException: If the company creation fails or if the company name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the company was created successfully.
    """
    await service.create(data)
    return {"message": "Company created successfully!"}
   
@router.put("/{company_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{company_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_company(company_id: int, data: CompanyUpdate, service: CompanyService = Depends(get_company_service)) -> dict[str,str]:
    """
    Update a company by its ID.

    Args:
        company_id (int): Unique identifier of the company.
        data (CompanyUpdate): The data used to update the company.
        service (CompanyService, optional): The service layer for handling
            company-related operations. This is injected automatically using
            `Depends(get_company_service)`.

    Raises:
        HTTPException: if the name already exist or if the company is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the company was updated successfully.
    """
    
    await service.update(company_id, data)
    return {"message": "the company updated successfully."}
    
@router.delete("/{company_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_company(company_id: int, service: CompanyService = Depends(get_company_service)) -> dict[str,str]:
    """
    Delete a company by its ID.

    Args:
        company_id (int): Unique identifier of the company.
        service (CompanyService, optional): The service layer for handling
            company-related operations. This is injected automatically using
            `Depends(get_company_service)`.

    Raises:
        HTTPException: if the company with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the company was deleted successfully.
    """

    await service.delete(company_id)
    return {"message": "the company deleted successfully."}
