from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.company_repository import CompanyRepository
from app.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyRead
from app.logic.base_service import BaseService, RepositoryType

class CompanyService(BaseService[CompanyRepository, CompanyCreate, CompanyUpdate, CompanyRead]):
    """
    Service for handling company-related operations.

    Inherits from BaseService to provide CRUD operations using the Company repository.
    """

    def __init__(self, repository: CompanyRepository, db: AsyncSession):
        """
        Initialize the CompanyService with the Company repository and an asynchronous database session.

        Args:
            repository (CompanyRepository): The repository for performing CRUD operations on Company entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)
