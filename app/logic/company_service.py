from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.company_repository import CompanyRepository
from app.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.company import Company

class CompanyService(
    BaseService[
        CompanyRepository, 
        CompanyCreate, 
        CompanyUpdate, 
        CompanyRead, 
        Company
        ]
    ):
    """
    Service for handling company-related operations.

    Inherits from BaseService to provide CRUD operations using the Company repository.
    """

    def __init__(self, repository: CompanyRepository, db: AsyncSession):
        """
        Initialize the CompanyService with the Company repository and an asynchronous database session.

        Args:
            repository (CompanyRepository): The repository for performing CRUD operations on Company entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)

    async def create(self, data: CompanyCreate) -> Company:
        """
        Create a new instance of the company repository

        Args:
            data (CompanyCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Company: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Company name already exists")
        return await super().create(data)