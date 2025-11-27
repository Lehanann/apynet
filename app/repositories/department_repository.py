from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate


class DepartmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, department_id: int):
        request = await self.db.execute(select(Department).where(Department.id_department == department_id))
        return request.scalars().first()
    
    async def get_by_name(self, dname: str):
        request = await self.db.execute(select(Department).where(Department.name == dname))
        return request.scalars().first()
    
    async def get_all(self):
        request = await self.db.execute(select(Department))
        return request.scalars().all()
    
    async def create(self, data: DepartmentCreate):
        department = Department(**data.model_dump())
        self.db.add(department)
        await self.db.commit()
        await self.db.refresh(department)
        return department
    
    async def update(self, department_id: int, data: DepartmentUpdate):
        department = await self.get_by_id(department_id)
        if not department:
            return None
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(department, key, value)
        await self.db.commit()
        await self.db.refresh(department)
        return department
    
    async def delete(self, department_id: int):
        department = await self.get_by_id(department_id)
        if not department:
            return False
        await self.db.delete(department)
        await self.db.commit()
        return True