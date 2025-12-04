from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.position_repository import PositionRepository
from app.schemas.position_schema import PositionCreate, PositionUpdate, PositionRead
from app.logic.base_service import BaseService, RepositoryType

class PositionService(BaseService[PositionRepository, PositionCreate, PositionUpdate, PositionRead]):
    """
    Service for handling position-related operations.

    Inherits from BaseService to provide CRUD operations using the Position repository.
    """

    def __init__(self, repository: PositionRepository, db: AsyncSession):
        """
        Initialize the PositionService with the Position repository and an asynchronous database session.

        Args:
            repository (PositionRepository): The repository for performing CRUD operations on Position entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)