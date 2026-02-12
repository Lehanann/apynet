from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.phone_assignment_service import PhoneAssignmentService
from app.schemas.phone_assignment_schema import PhoneAssignmentCreate, PhoneAssignmentRead, PhoneAssignmentUpdate
from app.repositories.phone_assignment_repository import PhoneAssignmentRepository

router = APIRouter(prefix="/phone-assignments", tags=["phone-assignments"])

def get_phone_assignment_service(db: AsyncSession = Depends(get_session)) -> PhoneAssignmentService:
    return PhoneAssignmentService(PhoneAssignmentRepository(db), db)

@router.get("/",response_model=list[PhoneAssignmentRead])
async def list_phone_assignments(service: PhoneAssignmentService = Depends(get_phone_assignment_service)):
    """
    Retrieve a list of all phone assignments from the database.

    This endpoint fetches all phone assignments stored in the database and returns 
    them in the format specified by the `PhoneAssignmentRead` schema.

    Args:
        service (PhoneAssignmentService, optional): The service layer for handling
            phone_assignment-related operations. This is injected automatically using
            `Depends(get_phone_assignment_service)`.

    Returns:
        List[PhoneAssignmentRead]: A list of phone assignments represented by the `PhoneAssignmentRead`
            schema, which includes relevant phone_assignment details such as name and ID.
    """
    return await service.get_all()

@router.get("/{phone_assignment_id}", response_model=PhoneAssignmentRead)
async def get_phone_assignment(phone_assignment_id: int, service: PhoneAssignmentService = Depends(get_phone_assignment_service)) -> PhoneAssignmentRead:
    """
    Retrieve phone_assignment by its ID from the database.

    This endpoint fetches a phone_assignment by its ID stored in the database and returns 
    them in the format specified by the `PhoneAssignmentRead` schema.

    Args:
        phone_assignment_id (int): Unique identifier of th ephone_assignment
        Args:
        service (PhoneAssignmentService, optional): The service layer for handling
            phone_assignment-related operations. This is injected automatically using
            `Depends(get_phone_assignment_service)`.

    Returns:
        phone_assignment (PhoneAssignmentRead): A phone_assignment represented by the `PhoneAssignmentRead`
            schema, which includes relevant phone_assignment details such as name and ID.
    """
    
    return await service.get_by_id(phone_assignment_id)
    
"""@router.get("/phone_assignment/{phone_assignment_name}", response_model=PhoneAssignmentRead)
async def get_phone_assignment_by_name(phone_assignment_name: str, service: PhoneAssignmentService = Depends(get_phone_assignment_service)):
    service = PhoneAssignmentService(db)
    return await service.get_phone_assignment_by_name(phone_assignment_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_phone_assignment(data: PhoneAssignmentCreate, service: PhoneAssignmentService = Depends(get_phone_assignment_service)) -> dict[str,str]:
    """
    Create a new phone_assignment.

    Args:
        data (PhoneAssignmentCreate): The datas used to create the phone_assignment.
        service (PhoneAssignmentService, optional): The service layer for handling
            phone_assignment-related operations. This is injected automatically using
            `Depends(get_phone_assignment_service)`.

    Raises:
        HTTPException: If the phone_assignment creation fails or if the phone_assignment name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the phone_assignment was created successfully.
    """
    await service.create(data)
    return {"message": "PhoneAssignment created successfully!"}
   
@router.put("/{phone_assignment_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{phone_assignment_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_phone_assignment(phone_assignment_id: int, data: PhoneAssignmentUpdate, service: PhoneAssignmentService = Depends(get_phone_assignment_service)) -> dict[str,str]:
    """
    Update a phone_assignment by its ID.

    Args:
        phone_assignment_id (int): Unique identifier of the phone_assignment.
        data (PhoneAssignmentUpdate): The data used to update the phone_assignment.
        service (PhoneAssignmentService, optional): The service layer for handling
            phone_assignment-related operations. This is injected automatically using
            `Depends(get_phone_assignment_service)`.

    Raises:
        HTTPException: if the name already exist or if the phone_assignment is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the phone_assignment was updated successfully.
    """
    
    await service.update(phone_assignment_id, data)
    return {"message": "the phone_assignment updated successfully."}
    
@router.delete("/{phone_assignment_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_phone_assignment(phone_assignment_id: int, service: PhoneAssignmentService = Depends(get_phone_assignment_service)) -> dict[str,str]:
    """
    Delete a phone_assignment by its ID.

    Args:
        phone_assignment_id (int): Unique identifier of the phone_assignment.
        service (PhoneAssignmentService, optional): The service layer for handling
            phone_assignment-related operations. This is injected automatically using
            `Depends(get_phone_assignment_service)`.

    Raises:
        HTTPException: if the phone_assignment with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the phone_assignment was deleted successfully.
    """

    await service.delete(phone_assignment_id)
    return {"message": "the phone_assignment deleted successfully."}
