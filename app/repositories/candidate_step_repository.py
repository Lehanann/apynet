from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.candidate_step import CandidateStep
from app.schemas.candidate_step_schema import CandidateStepCreate, CandidateStepUpdate
from app.repositories.base_repository import BaseRepository

class CandidateStepRepository(BaseRepository[CandidateStep, CandidateStepCreate, CandidateStepUpdate]):
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
        super().__init__(CandidateStep, db)