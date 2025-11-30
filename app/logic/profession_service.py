from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.profession_repository import ProfessionRepository
from app.schemas.profession_schema import ProfessionCreate, ProfessionUpdate, ProfessionRead
from app.logic.base_service import BaseService, RepositoryType

class ProfessionService(BaseService[ProfessionRepository, ProfessionCreate, ProfessionUpdate, ProfessionRead]):
    """
    Service for handling profession-related operations.

    Inherits from BaseService to provide CRUD operations using the Profession repository.
    """

    def __init__(self, repository: ProfessionRepository, db: AsyncSession):
        """
        Initialize the ProfessionService with the Profession repository and an asynchronous database session.

        Args:
            repository (ProfessionRepository): The repository for performing CRUD operations on Profession entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)
