from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.material_repository import MaterialRepository
from app.schemas.material_schema import MaterialCreate, MaterialUpdate, MaterialRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.material import Material

class MaterialService(
    BaseService[
        MaterialRepository, 
        MaterialCreate, 
        MaterialUpdate, 
        MaterialRead, 
        Material
        ]
    ):
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

    async def create(self, data: MaterialCreate) -> Material:
        """
        Create a new instance of the material repository.

        Args:
            data (MaterialCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Material: The newly created instance.
        """

        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Material name already exists")
        return await super().create(data)