from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.corporate import Corporate
from app.schemas.corporate_schema import CorporateCreate, CorporateUpdate

class CorporateRepository:
    """

    """
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self,corporate_id: int):
        """
        get one corporate by id
        :param corporate_id:
        :type corporate_id: int
        :return:
        :rtype:
        """
        result = await self.db.execute(select(Corporate).where(Corporate.id_corporate == corporate_id))
        return result.scalars().first()

    async def get_all(self):
        """
        get all corporates
        :return:
        :rtype:
        """
        result = await self.db.execute(select(Corporate))
        return result.scalars().all()

    async def get_by_name(self, name: str):
        """
        get one corporate by the name
        :param name:
        :type name:
        :return:
        :rtype:
        """
        result = await self.db.execute(select(Corporate).where(Corporate.name == name))
        return result.scalars().first()

    async def create(self, data: CorporateCreate):
        """
        Create a corporate
        :param data:
        :type data:
        :return:
        :rtype:
        """
        corporate = Corporate(**data.model_dump())
        self.db.add(corporate)
        await self.db.commit()
        await self.db.refresh(corporate)
        return corporate

    async def update(self, corporate_id: int, data: CorporateUpdate):
        """
        Update one corporate by id
        :param corporate_id:
        :type corporate_id:
        :param data:
        :type data:
        :return:
        :rtype:
        """
        corporate = await self.get_by_id(corporate_id)
        if not corporate:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(corporate, key, value)

        await self.db.commit()
        await self.db.refresh(corporate)
        return corporate

    async def delete(self, corporate_id: int):
        """
        Delete one company group by the id
        :param company_group_id:
        :type company_group_id:
        :return:
        :rtype:
        """
        corporate = await self.get_by_id(corporate_id)
        if not corporate:
            return False

        await self.db.delete(corporate)
        await self.db.commit()
        return True