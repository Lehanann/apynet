from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.phone_number_repository import PhoneNumberRepository
from app.schemas.phone_number_schema import PhoneNumberCreate, PhoneNumberUpdate, PhoneNumberRead
from app.logic.base_service import BaseService

class PhoneNumberService(BaseService[PhoneNumberRepository, PhoneNumberCreate, PhoneNumberUpdate, PhoneNumberRead]):
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