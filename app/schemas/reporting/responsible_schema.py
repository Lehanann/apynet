from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional


class DepartmentResponsibleRead(BaseModel):
    """
    Read-only schema for department responsibles view.
    Maps the SQL view: intranet.v_department_responsibles
    """

    id_department: int
    department_name: str
    company_name: str
    corporate_name: str

    id_employee: int
    first_name: str
    last_name: str

    work_email: Optional[str]
    personal_phone: Optional[str]

    profession_name: str
    position_name: str
    hire_date: date

    model_config = ConfigDict(from_attributes=True)

class ServiceResponsibleRead(BaseModel):
    """
    Read-only schema for service responsibles view.
    Maps the SQL view: intranet.v_service_responsibles
    """

    id_service: int
    service_name: str
    department_name: str
    company_name: str
    corporate_name: str

    id_employee: int
    first_name: str
    last_name: str

    work_email: Optional[str]
    personal_phone: Optional[str]

    profession_name: str
    position_name: str
    hire_date: date

    model_config = ConfigDict(from_attributes=True)

class StructureResponsibleRead(BaseModel):
    """
    Read-only schema for structure responsibles view.
    Maps the SQL view: intranet.v_structure_responsibles
    """

    structure_type: str  # 'department' | 'service'
    structure_id: int
    structure_name: str

    company_name: str
    corporate_name: str

    id_employee: int
    first_name: str
    last_name: str

    work_email: Optional[str]
    personal_phone: Optional[str]

    profession_name: str
    position_name: str
    hire_date: date

    model_config = ConfigDict(from_attributes=True)
