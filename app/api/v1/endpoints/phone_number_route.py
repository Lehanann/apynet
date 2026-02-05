from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.phone_number_service import PhoneNumberService
from app.schemas.phone_number_schema import PhoneNumberCreate, PhoneNumberRead, PhoneNumberUpdate
from app.repositories.phone_number_repository import PhoneNumberRepository

router = APIRouter(prefix="/phone-numbers", tags=["phone-numbers"])

def get_phone_number_service(db: AsyncSession = Depends(get_session)) -> PhoneNumberService:
    return PhoneNumberService(PhoneNumberRepository(db), db)

@router.get("/",response_model=list[PhoneNumberRead])
async def list_phone_numbers(service: PhoneNumberService = Depends(get_phone_number_service)):
    """
    Retrieve a list of all phone_numbers from the database.

    This endpoint fetches all phone_numbers stored in the database and returns 
    them in the format specified by the `PhoneNumberRead` schema.

    Args:
        service (PhoneNumberService, optional): The service layer for handling
            phone_number-related operations. This is injected automatically using
            `Depends(get_phone_number_service)`.

    Returns:
        List[PhoneNumberRead]: A list of phone_numbers represented by the `PhoneNumberRead`
            schema, which includes relevant phone_number details such as name and ID.
    """
    return await service.get_all()

@router.get("/{phone_number_id}", response_model=PhoneNumberRead)
async def get_phone_number(phone_number_id: int, service: PhoneNumberService = Depends(get_phone_number_service)) -> PhoneNumberRead:
    """
    Retrieve phone_number by its ID from the database.

    This endpoint fetches a phone_number by its ID stored in the database and returns 
    them in the format specified by the `PhoneNumberRead` schema.

    Args:
        phone_number_id (int): Unique identifier of th ephone_number
        Args:
        service (PhoneNumberService, optional): The service layer for handling
            phone_number-related operations. This is injected automatically using
            `Depends(get_phone_number_service)`.

    Returns:
        phone_number (PhoneNumberRead): A phone_number represented by the `PhoneNumberRead`
            schema, which includes relevant phone_number details such as name and ID.
    """
    
    return await service.get_by_id(phone_number_id)
    
"""@router.get("/phone_number/{phone_number_name}", response_model=PhoneNumberRead)
async def get_phone_number_by_name(phone_number_name: str, service: PhoneNumberService = Depends(get_phone_number_service)):
    service = PhoneNumberService(db)
    return await service.get_phone_number_by_name(phone_number_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_phone_number(data: PhoneNumberCreate, service: PhoneNumberService = Depends(get_phone_number_service)) -> dict[str,str]:
    """
    Create a new phone_number.

    Args:
        data (PhoneNumberCreate): The datas used to create the phone_number.
        service (PhoneNumberService, optional): The service layer for handling
            phone_number-related operations. This is injected automatically using
            `Depends(get_phone_number_service)`.

    Raises:
        HTTPException: If the phone_number creation fails or if the phone_number name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the phone_number was created successfully.
    """
    await service.create(data)
    return {"message": "PhoneNumber created successfully!"}
   
@router.put("/{phone_number_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{phone_number_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_phone_number(phone_number_id: int, data: PhoneNumberUpdate, service: PhoneNumberService = Depends(get_phone_number_service)) -> dict[str,str]:
    """
    Update a phone_number by its ID.

    Args:
        phone_number_id (int): Unique identifier of the phone_number.
        data (PhoneNumberUpdate): The data used to update the phone_number.
        service (PhoneNumberService, optional): The service layer for handling
            phone_number-related operations. This is injected automatically using
            `Depends(get_phone_number_service)`.

    Raises:
        HTTPException: if the name already exist or if the phone_number is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the phone_number was updated successfully.
    """
    
    await service.update(phone_number_id, data)
    return {"message": "the phone_number updated successfully."}
    
@router.delete("/{phone_number_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_phone_number(phone_number_id: int, service: PhoneNumberService = Depends(get_phone_number_service)) -> dict[str,str]:
    """
    Delete a phone_number by its ID.

    Args:
        phone_number_id (int): Unique identifier of the phone_number.
        service (PhoneNumberService, optional): The service layer for handling
            phone_number-related operations. This is injected automatically using
            `Depends(get_phone_number_service)`.

    Raises:
        HTTPException: if the phone_number with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the phone_number was deleted successfully.
    """

    await service.delete(phone_number_id)
    return {"message": "the phone_number deleted successfully."}
