from sqlalchemy.ext.asyncio import AsyncSession
from app.models.service import Service
from app.schemas.service_schema import ServiceCreate, ServiceUpdate
from app.repositories.base_repository import BaseRepository

class ServiceRepository(BaseRepository[Service, ServiceCreate, ServiceUpdate]):
    """
    Repository handling CRUD operations for the Service model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Service model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Service repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Service, db)