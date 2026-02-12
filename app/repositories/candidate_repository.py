from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.candidate import Candidate
from app.schemas.candidate_schema import CandidateCreate, CandidateUpdate
from app.repositories.base_repository import BaseRepository

class CandidateRepository(BaseRepository[Candidate, CandidateCreate, CandidateUpdate]):
    """
    Repository handling CRUD operations for the Candidate model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Candidate model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the company repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Candidate, db)