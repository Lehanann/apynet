from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.company import Company
from app.schemas.company_schema import CompanyCreate, CompanyUpdate
from app.repositories.base_repository import BaseRepository

class CompanyRepository(BaseRepository[Company, CompanyCreate, CompanyUpdate]):
    """
    Repository handling CRUD operations for the Company model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Company model,
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
        super().__init__(Company, db)