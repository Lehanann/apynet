from typing import TypeVar, Generic

# Type variable pour le modèle utilisé
ModelType = TypeVar("ModelType")

class NameSearchRepositoryMixin(Generic[ModelType]):
    """
    Mixin providing a generic method to fetch an instance by its 'name' field.

    This assumes that the model has a 'name' attribute.
    """

    async def get_by_name(self, name: str) -> ModelType | None:
        """
        Retrieve a single model instance by its 'name' attribute.

        Args:
            name (str): The name of the instance to retrieve.

        Returns:
            ModelType | None: The instance if found, else None.
        """
        # On suppose que le repository qui hérite a défini get_one_by()
        return await self.get_one_by("name", name)