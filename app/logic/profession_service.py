from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.profession_repository import ProfessionRepository
from app.schemas.profession_schema import ProfessionCreate, ProfessionUpdate, ProfessionRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.profession import Profession

class ProfessionService(
    BaseService[
        ProfessionRepository, 
        ProfessionCreate, 
        ProfessionUpdate, 
        ProfessionRead, 
        Profession
        ]
    ):
    """
    Service for handling profession-related operations.

    Inherits from BaseService to provide CRUD operations using the Profession repository.
    """

    def __init__(self, repository: ProfessionRepository, db: AsyncSession):
        """
        Initialize the ProfessionService with the Profession repository and an asynchronous database session.

        Args:
            repository (ProfessionRepository): The repository for performing CRUD operations on Profession entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)

    async def create(self, data: ProfessionCreate) -> Profession:
        """
        Create a new instance of the profession repository.

        Args:
            data (ProfessionCreate): Schema containing fields to create the new instance.

        Raises:
            HTTPException: if the name already exists in the repository.

        Returns:
            Profession: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Profession name already exists")
        return await super().create(data)
