from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.corporate_repository import CorporateRepository
from app.schemas.corporate_schema import CorporateCreate, CorporateUpdate, CorporateRead
from app.logic.base_service import BaseService, RepositoryType

class CorporateService(BaseService[CorporateRepository, CorporateCreate, CorporateUpdate, CorporateRead]):
    """
    Service for handling corporate-related operations.

    Inherits from BaseService to provide CRUD operations using the Corporate repository.
    """

    def __init__(self, repository: CorporateRepository, db: AsyncSession):
        """
        Initialize the CorporateService with the Corporate repository and an asynchronous database session.

        Args:
            repository (CorporateRepository): The repository for performing CRUD operations on Corporate entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)