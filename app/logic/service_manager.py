from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.service_repository import ServiceRepository
from app.schemas.service_schema import ServiceCreate, ServiceUpdate, ServiceRead
from app.logic.base_service import BaseService, RepositoryType

class ServiceManager(BaseService[ServiceRepository, ServiceCreate, ServiceUpdate, ServiceRead]):
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