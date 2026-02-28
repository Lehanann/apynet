from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.phone_number import PhoneNumber
from app.repositories.phone_number_repository import PhoneNumberRepository
from app.schemas.phone_number_schema import PhoneNumberCreate, PhoneNumberUpdate, PhoneNumberRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.phone_number import PhoneNumber

class PhoneNumberService(
    BaseService[
        PhoneNumberRepository, 
        PhoneNumberCreate, 
        PhoneNumberUpdate, 
        PhoneNumberRead, 
        PhoneNumber
        ]
    ):
    """
    Service for handling Phone number -related operations.

    Inherits from BaseService to provide CRUD operations using the PhoneNumber repository.
    """

    def __init__(self, repository: PhoneNumberRepository, db: AsyncSession):
        """
        Initialize the PhoneNumberService with the PhoneNumber repository and an asynchronous database session.

        Args:
            repository (PhoneNumberRepository): The repository for performing CRUD operations on PhoneNumber entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)

    async def create(self, data: PhoneNumberCreate) -> PhoneNumber:
        """
        Create a new instance of the phone number repository.

        Args:
            data (PhoneNumberCreate): Schema containing fields to create the new instance

        Raises:
            HTTPException: if the 'internal phone' already exists in the repository.

        Returns:
            PhoneNumber: The newly created instance.
        """
        if await self.repository.get_by_internal_number(data.internal_number):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This internal phone already exists.")
        return await super().create(data)
    
    async def update(self, id: int, data: PhoneNumberUpdate) -> PhoneNumber:
        """_summary_

        Args:
            id (int): _description_
            data (PhoneNumberUpdate): _description_

        Raises:
            HTTPException: _description_

        Returns:
            PhoneNumber: _description_
        """
        if data.internal_number:
            existing = await self.repository.get_by_internal_number(data.internal_number)

        if existing and existing.id_phone != id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A phone number with internal phone already exists.")
        
        return await super().update(id, data)
