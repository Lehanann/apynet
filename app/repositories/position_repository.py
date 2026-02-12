from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.position import Position
from app.schemas.position_schema import PositionCreate, PositionUpdate
from app.repositories.base_repository import BaseRepository

class PositionRepository(BaseRepository[Position, PositionCreate, PositionUpdate]):
    """
    Repository handling CRUD operations for the Position model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Position model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Position repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Position, db)