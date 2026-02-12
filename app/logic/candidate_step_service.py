from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.candidate_step_repository import CandidateStepRepository
from app.schemas.candidate_step_schema import CandidateStepCreate, CandidateStepUpdate, CandidateStepRead
from app.logic.base_service import BaseService, RepositoryType

class CandidateStepService(BaseService[CandidateStepRepository, CandidateStepCreate, CandidateStepUpdate, CandidateStepRead]):
    """
    Service for handling company-related operations.

    Inherits from BaseService to provide CRUD operations using the Company repository.
    """

    def __init__(self, repository: CandidateStepRepository, db: AsyncSession):
        """
        Initialize the CompanyService with the Company repository and an asynchronous database session.

        Args:
            repository (CompanyRepository): The repository for performing CRUD operations on Company entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)