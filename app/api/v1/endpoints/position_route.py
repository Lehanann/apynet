from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.position_service import PositionService
from app.schemas.position_schema import PositionCreate, PositionRead, PositionUpdate
from app.repositories.position_repository import PositionRepository

router = APIRouter(prefix="/positions", tags=["positions"])

def get_position_service(db: AsyncSession = Depends(get_session)) -> PositionService:
    return PositionService(PositionRepository(db), db)

@router.get("/",response_model=list[PositionRead])
async def list_positions(service: PositionService = Depends(get_position_service)):
    """
    Retrieve a list of all positions from the database.

    This endpoint fetches all positions stored in the database and returns 
    them in the format specified by the `PositionRead` schema.

    Args:
        service (PositionService, optional): The service layer for handling
            position-related operations. This is injected automatically using
            `Depends(get_position_service)`.

    Returns:
        List[PositionRead]: A list of positions represented by the `PositionRead`
            schema, which includes relevant position details such as name and ID.
    """
    return await service.get_all()

@router.get("/{position_id}", response_model=PositionRead)
async def get_position(position_id: int, service: PositionService = Depends(get_position_service)) -> PositionRead:
    """
    Retrieve position by its ID from the database.

    This endpoint fetches a position by its ID stored in the database and returns 
    them in the format specified by the `PositionRead` schema.

    Args:
        position_id (int): Unique identifier of th eposition
        Args:
        service (PositionService, optional): The service layer for handling
            position-related operations. This is injected automatically using
            `Depends(get_position_service)`.

    Returns:
        position (PositionRead): A position represented by the `PositionRead`
            schema, which includes relevant position details such as name and ID.
    """
    
    return await service.get_by_id(position_id)
    
"""@router.get("/position/{position_name}", response_model=PositionRead)
async def get_position_by_name(position_name: str, service: PositionService = Depends(get_position_service)):
    service = PositionService(db)
    return await service.get_position_by_name(position_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_position(data: PositionCreate, service: PositionService = Depends(get_position_service)) -> dict[str,str]:
    """
    Create a new position.

    Args:
        data (PositionCreate): The datas used to create the position.
        service (PositionService, optional): The service layer for handling
            position-related operations. This is injected automatically using
            `Depends(get_position_service)`.

    Raises:
        HTTPException: If the position creation fails or if the position name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the position was created successfully.
    """
    await service.create(data)
    return {"message": "Position created successfully!"}
   
@router.put("/{position_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{position_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_position(position_id: int, data: PositionUpdate, service: PositionService = Depends(get_position_service)) -> dict[str,str]:
    """
    Update a position by its ID.

    Args:
        position_id (int): Unique identifier of the position.
        data (PositionUpdate): The data used to update the position.
        service (PositionService, optional): The service layer for handling
            position-related operations. This is injected automatically using
            `Depends(get_position_service)`.

    Raises:
        HTTPException: if the name already exist or if the position is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the position was updated successfully.
    """
    
    await service.update(position_id, data)
    return {"message": "the position updated successfully."}
    
@router.delete("/{position_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_position(position_id: int, service: PositionService = Depends(get_position_service)) -> dict[str,str]:
    """
    Delete a position by its ID.

    Args:
        position_id (int): Unique identifier of the position.
        service (PositionService, optional): The service layer for handling
            position-related operations. This is injected automatically using
            `Depends(get_position_service)`.

    Raises:
        HTTPException: if the position with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the position was deleted successfully.
    """

    await service.delete(position_id)
    return {"message": "the position deleted successfully."}
