from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.service_repository import ServiceRepository
from app.schemas.service_schema import ServiceCreate, ServiceUpdate, ServiceRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.service import Service

class ServiceManager(
    BaseService[
        ServiceRepository, 
        ServiceCreate, 
        ServiceUpdate, 
        ServiceRead, 
        Service
        ]
    ):
    """
    Service for handling service-related operations.

    Inherits from BaseService to provide CRUD operations using the Service repository.
    """

    def __init__(self, repository: ServiceRepository, db: AsyncSession):
        """
        Initialize the ServiceManager with the Service repository and an asynchronous database session.

        Args:
            repository (ServiceRepository): The repository for performing CRUD operations on Service entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)
    
    async def create(self, data: ServiceCreate) -> Service:
        """
        Create a new instance of the service repository.

        Args:
            data (ServiceCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Service: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Service name already exists")
        return await super().create(data)