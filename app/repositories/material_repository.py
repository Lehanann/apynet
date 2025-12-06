from sqlalchemy.ext.asyncio import AsyncSession
from app.models.material import Material
from app.schemas.material_schema import MaterialCreate, MaterialUpdate
from app.repositories.base_repository import BaseRepository

class MaterialRepository(BaseRepository[Material, MaterialCreate, MaterialUpdate]):
    """
    Repository handling CRUD operations for the Material model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Material model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Material repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Material, db)