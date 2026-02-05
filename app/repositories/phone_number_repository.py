from sqlalchemy.ext.asyncio import AsyncSession
from app.models.phone_number import PhoneNumber
from app.schemas.phone_number_schema import PhoneNumberCreate, PhoneNumberUpdate
from app.repositories.base_repository import BaseRepository

class PhoneNumberRepository(BaseRepository[PhoneNumber, PhoneNumberCreate, PhoneNumberUpdate]):
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