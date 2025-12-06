from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.material_repository import MaterialRepository
from app.schemas.material_schema import MaterialCreate, MaterialUpdate, MaterialRead
from app.logic.base_service import BaseService

class MaterialService(BaseService[MaterialRepository, MaterialCreate, MaterialUpdate, MaterialRead]):
    """
    Service for handling material-related operations.

    Inherits from BaseService to provide CRUD operations using the Material repository.
    """
    def __init__(self, repository: MaterialRepository, db: AsyncSession):
        """
        Initialize the MaterialService with the Material repository and an asynchronous database session.

        Args:
            repository (MaterialRepository): The repository for performing CRUD operations on Material entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)