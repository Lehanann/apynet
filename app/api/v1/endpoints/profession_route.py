from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.profession_service import ProfessionService
from app.schemas.profession_schema import ProfessionCreate, ProfessionRead, ProfessionUpdate
from app.repositories.profession_repository import ProfessionRepository

router = APIRouter(prefix="/professions", tags=["professions"])

def get_profession_service(db: AsyncSession = Depends(get_session)) -> ProfessionService:
    return ProfessionService(ProfessionRepository(db), db)

@router.get("/",response_model=list[ProfessionRead])
async def list_professions(service: ProfessionService = Depends(get_profession_service)):
    """
    Retrieve a list of all professions from the database.

    This endpoint fetches all professions stored in the database and returns 
    them in the format specified by the `ProfessionRead` schema.

    Args:
        service (ProfessionService, optional): The service layer for handling
            profession-related operations. This is injected automatically using
            `Depends(get_profession_service)`.

    Returns:
        List[ProfessionRead]: A list of professions represented by the `ProfessionRead`
            schema, which includes relevant profession details such as name and ID.
    """
    return await service.get_all()

@router.get("/{profession_id}", response_model=ProfessionRead)
async def get_profession(profession_id: int, service: ProfessionService = Depends(get_profession_service)) -> ProfessionRead:
    """
    Retrieve profession by its ID from the database.

    This endpoint fetches a profession by its ID stored in the database and returns 
    them in the format specified by the `ProfessionRead` schema.

    Args:
        profession_id (int): Unique identifier of th eprofession
        Args:
        service (ProfessionService, optional): The service layer for handling
            profession-related operations. This is injected automatically using
            `Depends(get_profession_service)`.

    Returns:
        profession (ProfessionRead): A profession represented by the `ProfessionRead`
            schema, which includes relevant profession details such as name and ID.
    """
    
    return await service.get_by_id(profession_id)
    
"""@router.get("/profession/{profession_name}", response_model=ProfessionRead)
async def get_profession_by_name(profession_name: str, service: ProfessionService = Depends(get_profession_service)):
    service = ProfessionService(db)
    return await service.get_profession_by_name(profession_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_profession(data: ProfessionCreate, service: ProfessionService = Depends(get_profession_service)) -> dict[str,str]:
    """
    Create a new profession.

    Args:
        data (ProfessionCreate): The datas used to create the profession.
        service (ProfessionService, optional): The service layer for handling
            profession-related operations. This is injected automatically using
            `Depends(get_profession_service)`.

    Raises:
        HTTPException: If the profession creation fails or if the profession name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the profession was created successfully.
    """
    await service.create(data)
    return {"message": "Profession created successfully!"}
   
@router.put("/{profession_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{profession_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_profession(profession_id: int, data: ProfessionUpdate, service: ProfessionService = Depends(get_profession_service)) -> dict[str,str]:
    """
    Update a profession by its ID.

    Args:
        profession_id (int): Unique identifier of the profession.
        data (ProfessionUpdate): The data used to update the profession.
        service (ProfessionService, optional): The service layer for handling
            profession-related operations. This is injected automatically using
            `Depends(get_profession_service)`.

    Raises:
        HTTPException: if the name already exist or if the profession is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the profession was updated successfully.
    """
    
    await service.update(profession_id, data)
    return {"message": "the profession updated successfully."}
    
@router.delete("/{profession_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_profession(profession_id: int, service: ProfessionService = Depends(get_profession_service)) -> dict[str,str]:
    """
    Delete a profession by its ID.

    Args:
        profession_id (int): Unique identifier of the profession.
        service (ProfessionService, optional): The service layer for handling
            profession-related operations. This is injected automatically using
            `Depends(get_profession_service)`.

    Raises:
        HTTPException: if the profession with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the profession was deleted successfully.
    """

    await service.delete(profession_id)
    return {"message": "the profession deleted successfully."}
