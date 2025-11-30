from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.corporate_service import CorporateService
from app.schemas.corporate_schema import CorporateCreate, CorporateRead, CorporateUpdate
from app.repositories.corporate_repository import CorporateRepository

router = APIRouter(prefix="/corporates", tags=["corporates"])

def get_corporate_service(db: AsyncSession = Depends(get_session)) -> CorporateService:
    return CorporateService(CorporateRepository(db), db)

@router.get("/",response_model=list[CorporateRead])
async def list_corporates(service: CorporateService = Depends(get_corporate_service)):
    """
    Retrieve a list of all corporates from the database.

    This endpoint fetches all corporates stored in the database and returns 
    them in the format specified by the `CorporateRead` schema.

    Args:
        service (CorporateService, optional): The service layer for handling
            corporate-related operations. This is injected automatically using
            `Depends(get_corporate_service)`.

    Returns:
        List[CorporateRead]: A list of corporates represented by the `CorporateRead`
            schema, which includes relevant corporate details such as name and ID.
    """
    return await service.get_all()

@router.get("/{corporate_id}", response_model=CorporateRead)
async def get_corporate(corporate_id: int, service: CorporateService = Depends(get_corporate_service)) -> CorporateRead:
    """
    Retrieve corporate by its ID from the database.

    This endpoint fetches a corporate by its ID stored in the database and returns 
    them in the format specified by the `CorporateRead` schema.

    Args:
        corporate_id (int): Unique identifier of th ecorporate
        Args:
        service (CorporateService, optional): The service layer for handling
            corporate-related operations. This is injected automatically using
            `Depends(get_corporate_service)`.

    Returns:
        corporate (CorporateRead): A corporate represented by the `CorporateRead`
            schema, which includes relevant corporate details such as name and ID.
    """
    
    return await service.get_by_id(corporate_id)
    
"""@router.get("/corporate/{corporate_name}", response_model=CorporateRead)
async def get_corporate_by_name(corporate_name: str, service: CorporateService = Depends(get_corporate_service)):
    service = CorporateService(db)
    return await service.get_corporate_by_name(corporate_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_corporate(data: CorporateCreate, service: CorporateService = Depends(get_corporate_service)) -> dict[str,str]:
    """
    Create a new corporate.

    Args:
        data (CorporateCreate): The datas used to create the corporate.
        service (CorporateService, optional): The service layer for handling
            corporate-related operations. This is injected automatically using
            `Depends(get_corporate_service)`.

    Raises:
        HTTPException: If the corporate creation fails or if the corporate name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the corporate was created successfully.
    """
    await service.create(data)
    return {"message": "Corporate created successfully!"}
   
@router.put("/{corporate_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{corporate_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_corporate(corporate_id: int, data: CorporateUpdate, service: CorporateService = Depends(get_corporate_service)) -> dict[str,str]:
    """
    Update a corporate by its ID.

    Args:
        corporate_id (int): Unique identifier of the corporate.
        data (CorporateUpdate): The data used to update the corporate.
        service (CorporateService, optional): The service layer for handling
            corporate-related operations. This is injected automatically using
            `Depends(get_corporate_service)`.

    Raises:
        HTTPException: if the name already exist or if the corporate is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the corporate was updated successfully.
    """
    
    await service.update(corporate_id, data)
    return {"message": "the corporate updated successfully."}
    
@router.delete("/{corporate_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_corporate(corporate_id: int, service: CorporateService = Depends(get_corporate_service)) -> dict[str,str]:
    """
    Delete a corporate by its ID.

    Args:
        corporate_id (int): Unique identifier of the corporate.
        service (CorporateService, optional): The service layer for handling
            corporate-related operations. This is injected automatically using
            `Depends(get_corporate_service)`.

    Raises:
        HTTPException: if the corporate with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the corporate was deleted successfully.
    """

    await service.delete(corporate_id)
    return {"message": "the corporate deleted successfully."}
