from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.site_repository import SiteRepository
from app.schemas.site_schema import SiteCreate, SiteUpdate, SiteRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.site import Site

class SiteService(
    BaseService[
        SiteRepository, 
        SiteCreate, 
        SiteUpdate, 
        SiteRead,
        Site
        ]
    ):
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

    async def create(self, data: SiteCreate) -> Site:
        """
        Create a new instance of the site repository.

        Args:
            data (SiteCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Site: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Site name already exists")
        return await super().create(data)