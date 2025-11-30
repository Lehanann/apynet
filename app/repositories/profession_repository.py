from sqlalchemy.ext.asyncio import AsyncSession
from app.models.profession import Profession
from app.schemas.profession_schema import ProfessionCreate, ProfessionUpdate
from app.repositories.base_repository import BaseRepository

class ProfessionRepository(BaseRepository[Profession, ProfessionCreate, ProfessionUpdate]):
    """
    Repository handling CRUD operations for the Profession model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Profession model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Profession repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Profession, db)