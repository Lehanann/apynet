from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tables.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate
from app.repositories.base_repository import BaseRepository
from app.repositories.mixins.filterable_repository import FilterableRepositoryMixin

class EmployeeRepository(
    BaseRepository[
        Employee, 
        EmployeeCreate, 
        EmployeeUpdate
        ], 
    FilterableRepositoryMixin[Employee]
    ):
    """
    Repository handling CRUD operations for the Employee model.

    Inherits generic CRUD functionality from BaseRepository.

    This repository specializes the BaseRepository for the Employee model,
    providing type-specific hints and schemas.

    Attributes:
        db (AsyncSession): The asynchronous database session used for SQL operations.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the Employee repository with a database session.

        Args:
            db (AsyncSession): The asynchronous database session used
                to perform SQL operations.
        """
        super().__init__(Employee, db)

    async def get_by_personal_email(self, personal_email: str) -> Employee | None:
        """Retrieve an employee instance by its personal email.

        Args:
            email (str): Personal email of the employee.

        Returns:
            Employee | None: The employee if found, otherwise None
        """
        return await self.get_one_by("personal_email", personal_email)

    async def get_by_company(self, company_id: int) -> list[Employee]:
        """Retrieve all instances of employees by company from database.

        Args:
            company_id (int): The unique identifier of the company.

        Returns:
            List[Employee]: A list of employees by company.
        """
        return await self.get_many_by("company_id", company_id)

    async def get_active_employees(self) -> list[Employee]:
        """Retrieve all instances of active employees from database.

        Returns:
            List[Employee]: A list of all active employees.
        """
        return await self.get_many_by("archived", False)
    
    async def get_by_matricule(self, matricule: int) -> Employee | None:
        """Retrieve a model instance by matricule

        Args:
            matricule (int): the unique matricule of the employee.

        Returns:
            Employee | None: The employee if found, otherwise None.
        """
        return await self.get_one_by("matricule", matricule)