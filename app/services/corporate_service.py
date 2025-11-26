from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.corporate_repository import CorporateRepository
from app.schemas.corporate_schema import CorporateCreate, CorporateUpdate


class CorporateService:
    def __init__(self, db:AsyncSession):
        self.repositories = CorporateRepository(db)

    async def list_corporates(self):
        """
        Docstring for list_corporates
        return a list of corporates in the db
        """
        return await self.repositories.get_all()

    async def get_corporate(self,corporate_id: int):
        """
        Docstring for get_corporate
        return one corporate by the id
        
        :param corporate_id: corporate identifiant
        :type corporate_id: int
        """
        corporate = await self.repositories.get_by_id(corporate_id)
        if not corporate:
            raise ValueError("Corporate not found")
        return corporate

    async def create_corporate(self, data: CorporateCreate):
        """
        Docstring for create_corporate
        create a corporate in the db      
  
        :param data: Object based on the pydantic schema 'CorporateCreate' containing necessary field "name"
        :type data: CorporateCreate
        """
        if await self.repositories.get_by_name(data.name):
            raise ValueError(f"the corporate {data.name} already exists!")
        return await self.repositories.create(data)

    async def update_corporate(self,corporate_id: int, data: CorporateUpdate):
        """
        Docstring for update_corporate
        update a corporate in the db

        :param corporate_id: identifiant of carporate
        :type corporate_id: int
        :param data: object based on the pydantic schema 'CorporateUpdate'
        :type data: CorporateUpdate
        """
        corporate = await self.repositories.get_by_id(corporate_id)
        if not corporate:
            raise ValueError("corporate not found")

        if data.name and data.name != corporate.name:
            if await self.repositories.get_by_name(data.name):
                raise ValueError(f"The name {data.name} already exist")

        return await self.repositories.update(corporate_id, data)

    async def delete_corporate(self, corporate_id: int):
        """
        Docstring for delete_corporate
        delete a corporate by id

        :param corporate_id: identifiant of corporate
        :type corporate_id: int
        """
        deleted = await self.repositories.delete(corporate_id)
        if not deleted:
            raise ValueError("corporate cannot deleted!")
        return True






