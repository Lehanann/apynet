from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.corporate import Corporate
from app.schemas.corporate_schema import CorporateCreate, CorporateUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin
from app.repositories.mixins.name_search_repository import NameSearchRepositoryMixin

class CorporateRepository(
    BaseRepository[
        Corporate, 
        CorporateCreate, 
        CorporateUpdate
        ], 
    FilterableRepositoryMixin[Corporate], 
    NameSearchRepositoryMixin[Corporate]
    ):
    """
    Repository handling CRUD operations for the Corporate model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Corporate model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self,db: AsyncSession):
        """
        Initialize the Corporate repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Corporate, db)