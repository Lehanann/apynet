from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.phone_number import PhoneNumber
from app.schemas.phone_number_schema import PhoneNumberCreate, PhoneNumberUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin

class PhoneNumberRepository(
    BaseRepository[
        PhoneNumber, 
        PhoneNumberCreate, 
        PhoneNumberUpdate
        ], 
    FilterableRepositoryMixin[PhoneNumber]
    ):
    """
    Repository handling CRUD operations for the PhoneNumber model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the PhoneNumber model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """

    def __init__(self, db: AsyncSession):
        """
        Initialize the user account repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(PhoneNumber, db)

    async def get_by_internal_number(self, internal_number: str) -> PhoneNumber | None:
        """Retrieve a phone number instance by its internal number.

        Args:
            internal_number (str): internal number of phone number.

        Returns:
            PhoneNumber | None: Phone number instance if found, otherwise None.
        """
        return await self.get_one_by("internal_number", internal_number)
    
    