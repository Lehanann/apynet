from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.company import Company
from app.schemas.company_schema import CompanyCreate, CompanyUpdate

class CompanyRepository:
    
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, company_id: int):
        
        result = await self.db.execute(select(Company).where(Company.id_company == company_id))
        return result.scalars().first()
    
    async def get_by_name(self, name):

        result = await self.db.execute(select(Company).where(Company.name == name))
        return result.scalars().first()        

    async def get_all(self):

        result = await self.db.execute(select(Company))
        return result.scalars().all()
    
    async def create(self, data: CompanyCreate):

        company = Company(**data.model_dump())
        self.db.add(company)
        await self.db.commit()
        await self.db.refresh(company)
        return company
    
    async def update(self, company_id: int, data: CompanyUpdate):

        company = await self.get_by_id(company_id)
        if not company:
            return None
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(company, key, value)

        await self.db.commit()
        await self.db.refresh(company)
        return company
    
    async def delete(self, company_id: int):
        company = await self.get_by_id(company_id)
        if not company:
            return False
        
        await self.db.delete(company)
        await self.db.commit()
        return True