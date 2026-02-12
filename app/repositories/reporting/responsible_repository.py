# app/domains/reporting/repositories/responsibles_repository.py
"""
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.views.responsible import DepartmentResponsible, ServiceResponsible, StructureResponsible

class ResponsibleRepository:
    
    Repository handling read-only queries for responsible views.
    

    def __init__(self, db: Session):
        self.db = db

    # ===============================
    # Department Responsibles
    # ===============================

    def get_department_responsibles(self):
        stmt = select(DepartmentResponsible)
        return self.db.execute(stmt).scalars().all()

    # ===============================
    # Service Responsibles
    # ===============================

    def get_service_responsibles(self):
        stmt = select(ServiceResponsible)
        return self.db.execute(stmt).scalars().all()

    # ===============================
    # Structure Responsibles
    # ===============================

    def get_structure_responsibles(self):
        stmt = select(StructureResponsible)
        return self.db.execute(stmt).scalars().all()
"""

# app/domains/reporting/repositories/responsibles_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.views.responsible import DepartmentResponsible, ServiceResponsible, StructureResponsible

class ResponsibleRepository:
    """
        Repository handling read-only queries for responsible views.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_departments(self):
        result = await self.session.execute(select(DepartmentResponsible))
        return result.scalars().all()

    async def get_all_services(self):
        result = await self.session.execute(select(ServiceResponsible))
        return result.scalars().all()
    
    async def get_all_structures(self):
        result = await self.session.execute(select(StructureResponsible))
        return result.scalars().all()