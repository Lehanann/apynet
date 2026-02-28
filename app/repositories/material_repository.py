from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.material import Material
from app.schemas.material_schema import MaterialCreate, MaterialUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin
from app.repositories.mixins.name_search_repository import NameSearchRepositoryMixin

class MaterialRepository(
    BaseRepository[
        Material, 
        MaterialCreate, 
        MaterialUpdate
        ], 
    FilterableRepositoryMixin[Material], 
    NameSearchRepositoryMixin[Material]
    ):
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