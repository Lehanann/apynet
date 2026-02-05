from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.site_repository import SiteRepository
from app.schemas.site_schema import SiteCreate, SiteUpdate, SiteRead
from app.logic.base_service import BaseService

class SiteService(BaseService[SiteRepository, SiteCreate, SiteUpdate, SiteRead]):
    """
    Service for handling Phone number -related operations.

    Inherits from BaseService to provide CRUD operations using the Site repository.
    """

    def __init__(self, repository: SiteRepository, db: AsyncSession):
        """
        Initialize the SiteService with the Site repository and an asynchronous database session.

        Args:
            repository (SiteRepository): The repository for performing CRUD operations on Site entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)