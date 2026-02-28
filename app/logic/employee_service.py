from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate, EmployeeRead
from app.logic.base_service import BaseService
from fastapi import HTTPException, status
from app.models.tables.employee import Employee
import uuid
from datetime import date
from app.infrastructure.storage.employee_document_manager import EmployeeDocumentManager
from app.core.settings import settings

class EmployeeService(
    BaseService[
        EmployeeRepository, 
        EmployeeCreate, 
        EmployeeUpdate, 
        EmployeeRead, 
        Employee
        ]
    ):
    """
    Service for handling employee-related operations.

    Inherits from BaseService to provide CRUD operations using the Employee repository.
    """
    
    def __init__(self, repository: EmployeeRepository, db: AsyncSession):
        """
        Initialize the EmployeenService with the Employee repository and an asynchronous database session.

        Args:
            repository (EmployeeRepository): The repository for performing CRUD operations on Employee entities.
            db (AsyncSession): The asynchronous database session used for SQL operations.
        """
        super().__init__(repository, db)

    async def create(self, data: EmployeeCreate) -> Employee:
        """
        Create a new instance of the employee repository.

        Args: 
            data (EmployeeCreate): Schema containing fields to create the new instance.
        
        Raises:
            HTTPException: if the matricule already exists in the repository.

        Returns:
            The newly created instance with added document_token's field.
        """

        if data.matricule:
            existing = await self.repository.get_by_matricule(
                data.matricule
            )
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"the matricule {data.matricule} already exists."
                )
        
        #employee = Employee(**data.model_dump())
        employee = await self.repository.create(data)


        document_manager = EmployeeDocumentManager(settings.DOCUMENT_ROOT)
        document_manager.create_workspace(str(employee.document_token))
       
        return employee

    async def update(self, id: int, data: EmployeeUpdate) -> Employee:
        """_summary_

        Args:
            id (int): _description_
            data (EmployeeUpdate): _description_

        Raises:
            HTTPException: _description_

        Returns:
            Employee: _description_
        """
        employee = await self.repository.get_by_id(id)

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        if data.matricule:
            existing = await self.repository.get_by_matricule(data.matricule)

            if existing and existing.id_employee != id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Employee with this matricule already exists."
                )

        update_dict = data.model_dump(exclude_unset=True)

        # --- LEAVE DATE BUSINESS RULE ---
        if "leave_date" in update_dict and update_dict["leave_date"] is not None:

            leave_date = update_dict["leave_date"]
            today = date.today()
            hire_date = employee.hire_date

            if leave_date < today:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="leave_date cannot be in the past."
                )

            if hire_date and leave_date <= hire_date:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="leave_date must be strictly greater than hire_date."
                )

            # Auto archive si valide
            update_dict["archived"] = leave_date < today

        enriched_data = data.model_copy(update=update_dict)

        return await super().update(id, enriched_data)

    async def archive(self, id: int) -> Employee:
        """Soft delete employee

        Args:
            id (int): _description_

        Raises:
            HTTPException: _description_

        Returns:
            Employee: _description_
        """
        employee = await self.repository.get_by_id(id)

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found."
            )

        employee.archived = True
        await self.db.commit()
        await self.db.refresh(employee)

        return employee