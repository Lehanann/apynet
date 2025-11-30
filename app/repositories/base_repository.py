from typing import TypeVar, Generic, Type, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel

# Type variables pour les modèles SQLAlchemy et les schémas Pydantic
ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Generic repository providing CRUD operations for a given SQLAlchemy model.

    Attributes:
        db (AsyncSession): The asynchronous database session.
        model (Type[ModelType]): The SQLAlchemy model class handled by the repository.
    """
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        """
        Initialize the repository with a model and a database session.

        Args:
            model (Type[ModelType]): The SQLAlchemy model class.
            db (AsyncSession): The asynchronous database session.
        """
        self.model = model
        self.db = db

    async def get_by_id(self, id: int) -> ModelType | None:
        """
        Retrieve a model instance by its ID.

        Args:
            id (int): The unique identifier of the instance.

        Returns:
            ModelType | None: The instance if found, otherwise None.
        """
        return await self.db.get(self.model, id)

    async def get_by_name(self, name: str) -> ModelType | None:
        """
        Retrieve a model instance by its name attribute.

        Args:
            name (str): The name of the instance.

        Returns:
            ModelType | None: The matching instance if found, otherwise None.
        """
        result = await self.db.execute(select(self.model).where(self.model.name == name))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[ModelType]:
        """
        Retrieve all instances of the model from the database.

        Returns:
            List[ModelType]: A list of all instances.
        """
        result = await self.db.execute(select(self.model))
        return result.scalars().all()

    async def create(self, data: CreateSchemaType) -> ModelType:
        """
        Create a new instance of the model.

        Args:
            data (CreateSchemaType): The schema containing fields to create the instance.

        Returns:
            ModelType: The newly created instance.
        """
        instance = self.model(**data.model_dump())
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def update(self, id: int, data: UpdateSchemaType) -> ModelType | None:
        """
        Update an existing instance of the model.

        Args:
            id (int): The ID of the instance to update.
            data (UpdateSchemaType): The schema containing fields to update.

        Returns:
            ModelType | None: The updated instance if exists, otherwise None.

        Side Effects:
            Commits changes to the database and refreshes the instance.
        """
        instance = await self.get_by_id(id)
        if not instance:
            return None

        update_data = data.model_dump(exclude_unset=True)
        if update_data:
            for key, value in update_data.items():
                setattr(instance, key, value)
            await self.db.commit()
            await self.db.refresh(instance)
        return instance

    async def delete(self, id: int) -> bool:
        """
        Delete an instance by its ID.

        Args:
            id (int): The ID of the instance to delete.

        Returns:
            bool: True if deletion succeeded, False if instance does not exist.

        Side Effects:
            Commits deletion to the database.
        """
        instance = await self.get_by_id(id)
        if not instance:
            return False
        await self.db.delete(instance)
        await self.db.commit()
        return True
