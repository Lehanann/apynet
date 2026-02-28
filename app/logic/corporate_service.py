from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.corporate_repository import CorporateRepository
from app.schemas.corporate_schema import CorporateCreate, CorporateUpdate, CorporateRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.corporate import Corporate

class CorporateService(
    BaseService[
        CorporateRepository, 
        CorporateCreate, 
        CorporateUpdate, 
        CorporateRead, 
        Corporate
        ]
    ):
    """
    Service for handling corporate-related operations.

    Inherits from BaseService to provide CRUD operations using the Corporate repository.
    """

    def __init__(self, repository: CorporateRepository, db: AsyncSession):
        """
        Initialize the CorporateService with the Corporate repository and an asynchronous database session.

        Args:
            repository (CorporateRepository): The repository for performing CRUD operations on Corporate entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)
    
    async def create(self, data: CorporateCreate) -> Corporate:
        """
        Create a new instance of the corporate repository.

        Args:
            data (CorporateCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Corporate: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Corporate name already exists")
        return await super().create(data)