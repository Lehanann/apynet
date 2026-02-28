from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.site import Site
from app.schemas.site_schema import SiteCreate, SiteUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin
from app.repositories.mixins.name_search_repository import NameSearchRepositoryMixin

class SiteRepository(
    BaseRepository[
        Site, 
        SiteCreate, 
        SiteUpdate
        ], 
    FilterableRepositoryMixin[Site], 
    NameSearchRepositoryMixin[Site]
    ):
    """
    Repository handling CRUD operations for the Site model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Site model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """

    def __init__(self, db: AsyncSession):
        """
        Initialize the user account repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Site, db)