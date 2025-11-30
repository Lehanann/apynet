from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic, Optional, Dict, List
from pydantic import BaseModel
from fastapi import HTTPException, status

RepositoryType = TypeVar("RepositoryType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)
ModelType = TypeVar("ModelType")

class BaseService(Generic[RepositoryType, CreateSchemaType, UpdateSchemaType, ReadSchemaType]):
    """
    Generic service that performs basic operations on repositories such as reading, creating, deleting, and updating.

    Attributes:
        repository (RepositoryType): A repository instance that handles CRUD operations for a specific model.
        db (AsyncSession): The asynchronous database session used to interact with the database.
    """
    def __init__(self, repository: RepositoryType, db: AsyncSession):
        """
        Initialize the service with a repository.

        Args:
            repository (RepositoryType): Repository instance that handles the CRUD operations.
            db (AsyncSession): The asynchronous database session.
        """
        self.repository = repository
        self.db = db

    async def get_by_id(self, id: int) ->ReadSchemaType:
        """
        Get a single item from the repository by its ID.

        Args:
            id (int): The ID of the instance to retrieve.

        Raises:
            HTTPException: If the ID of item is not found.

        Returns:
            Optional[ReadSchemaType]: The instance if found, otherwise None.
        """
        item = await self.repository.get_by_id(id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")
        return item
    
    async def get_all(self) -> List[ModelType]:
        """
        Get all item from the repository.

        Raises:
            HTTPException: if list of companies is empty.

        Returns:
            List[ModelType]: A list of all instances from the repository.
        """
        items = await self.repository.get_all()
        if not items:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found")
        return items

    async def create(self, data: CreateSchemaType) -> ModelType:
        """
        Create a new instance of the repository.

        Args:
            data (CreateSchemaType): The schema containing fields to create the instance.

        Raises:
            HTTPException: If the name already exists in the repository.

        Returns:
            ModelType: The newly created instance.
        """
        if await self.repository.get_by_name(data.name):
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail=f"The name {data.name} already exists!")  
        return await self.repository.create(data)
    
    async def update(self, id: int, data: UpdateSchemaType) -> ModelType:
        """
        Update an existing instance in the repository.

        Args:
            id (int): The ID of the instance to update.
            data (UpdateSchemaType): The schema containing fields to update.

        Raises:
            HTTPException: If the name already exists in the repository.
            HTTPException: If the item cannot be found by its ID.

        Returns:
            Optional[ModelType]: The updated instance.
        """
        if data.name and await self.repository.get_by_name(data.name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The name {data.name} already exists!")
        
        existing = await self.repository.get_by_id(id)
        if not existing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!")
        return await self.repository.update(id, data)
    
    async def delete(self, id: int) -> Dict[str, str]:
        """
        Delete an instance of the repository.

        Args:
            id (int): The ID of the instance to delete.

        Raises:
            ValueError: If the item doesn't exist or cannot be deleted.

        Returns:
            Dict[str, str]: A message indicating the success of the deletion.
        """
        deleted = await self.repository.delete(id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!")
        return deleted
