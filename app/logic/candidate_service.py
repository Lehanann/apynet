from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.candidate_repository import CandidateRepository
from app.schemas.candidate_schema import CandidateCreate, CandidateUpdate, CandidateRead
from app.logic.base_service import BaseService, RepositoryType

class CandidateService(BaseService[CandidateRepository, CandidateCreate, CandidateUpdate, CandidateRead]):
    """
    Service for handling company-related operations.

    Inherits from BaseService to provide CRUD operations using the Company repository.
    """

    def __init__(self, repository: CandidateRepository, db: AsyncSession):
        """
        Initialize the CompanyService with the Company repository and an asynchronous database session.

        Args:
            repository (CompanyRepository): The repository for performing CRUD operations on Company entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)