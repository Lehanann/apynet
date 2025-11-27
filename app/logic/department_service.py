from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.department_repository import DepartmentRepository
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate

class DepartmentService:

    def __init__(self, db: AsyncSession):
        self.repository = DepartmentRepository(db)

    async def list_departments(self):
        return await self.repository.get_all()
    
    async def get_department(self, department_id: int):
        department = await self.repository.get_by_id(department_id)
        if not department:
            raise ValueError("department not found!")
        return department
    
    async def get_department_by_name(self, department_name: str):
        department = await self.repository.get_by_name(department_name)
        if not department:
            raise ValueError("department not found!")
        return department
    
    async def create_department(self, data: DepartmentCreate):
        if await self.repository.get_by_name(data.name):
            raise ValueError(f"The department name: {data.name} already exists!")
        return await self.repository.create(data)
    
    async def update_department(self, department_id: int, data: DepartmentUpdate):
        department = await self.repository.get_by_id(department_id)
        if not department:
            raise ValueError("Department not found!")
        
        if data.name and data.name != department.name:
            if await self.repository.get_by_name(data.name):
                raise ValueError("The department name: {data.name} already exist")
            
        return await self.repository.update(department_id, data)
    
    async def delete_department(self, department_id: int):
        department = await self.repository.delete(department_id)
        if not department:
            raise ValueError("Department not found!")
        return {"message": "Department was deleted"}