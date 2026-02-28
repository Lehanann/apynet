from sqlalchemy import select
from typing import TypeVar, Generic, List, Any

ModelType = TypeVar("ModelType")

class FilterableRepositoryMixin(Generic[ModelType]):
    """
    Mixin providing reusable filtering methods.
    Requires self.model and self.db to exist.
    """
    async def get_one_by(self, field: str, value: Any) -> ModelType | None:
        result = await self.db.execute(select(self.model).where(getattr(self.model, field) == value))
        return result.scalar_one_or_none()

    async def get_many_by(self, field: str, value: Any) -> List[ModelType]:
        result = await self.db.execute(select(self.model).where(getattr(self.model, field) == value))
        return result.scalars().all()