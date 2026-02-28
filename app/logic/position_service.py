from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.position_repository import PositionRepository
from app.schemas.position_schema import PositionCreate, PositionUpdate, PositionRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.position import Position

class PositionService(
    BaseService[
        PositionRepository, 
        PositionCreate, 
        PositionUpdate, 
        PositionRead, 
        Position
        ]
    ):
    """
    Service for handling position-related operations.

    Inherits from BaseService to provide CRUD operations using the Position repository.
    """

    def __init__(self, repository: PositionRepository, db: AsyncSession):
        """
        Initialize the PositionService with the Position repository and an asynchronous database session.

        Args:
            repository (PositionRepository): The repository for performing CRUD operations on Position entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)

    async def create(self, data: PositionCreate) -> Position:
        """
        Create a new instance of the position repository.

        Args:
            data (PositionCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Position: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Positions name already exists")
        return await super().create(data)