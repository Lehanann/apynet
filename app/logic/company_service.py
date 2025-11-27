from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.company_repository import CompanyRepository
from app.schemas.company_schema import CompanyCreate, CompanyUpdate

class CompanyService:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = CompanyRepository(db)

    async def list_companies(self):
        return await self.repository.get_all()
    
    async def get_company(self, company_id: int):
        company = await self.repository.get_by_id(company_id)
        if not company:
            raise ValueError("Company not found!")
        
        return company
    
    async def get_company_by_name(self, company_name: str):
        company = await self.repository.get_by_name(company_name)
        if not company:
            raise ValueError("Company not found!")
        
        return company
    
    async def create_company(self, data: CompanyCreate):
        
        if await self.repository.get_by_name(data.name):
            raise ValueError(f'Error, the company name: {data.name} already exists!')
        
        return await self.repository.create(data)
    
    async def update_company(self, company_id: int, data: CompanyCreate):

        company = await self.repository.get_by_id(company_id)
        if not company:
            raise ValueError("Company not found!")
        
        if data.name and data.name != company.name:
            if await self.repository.get_by_name(data.name):
                raise ValueError(f"The name {data.name} already exist")

        return await self.repository.update(company_id, data)
    
    async def delete_company(self, company_id: int):
        company = await self.repository.delete(company_id)
        if not company:
            raise ValueError("Company cannot deleted!")
        return {"message": "company was successfully deleted!"}
        
