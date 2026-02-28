from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Any
from datetime import date
from app.utils.gender_enum import GenderEnum


class EmployeeBase(BaseModel):
    """
    Base schema for the employee, shared by create, update, and read operations and inherited by other schemas.

    Attributes:
        matricule (int): Matricule of the Employee.
        first_name (str): First name of the employee.
        last_name (str): Last name of the employee.
        birth_date (date): Birth date of the employee.
        gender (GenderEnum): Gender of the employee.
        address (str): Home address of the employee.
        personal_email (str): Personal email address of the employee.
        personal_phone (str): Personal phone number of the employee.
        social_security_number (str): Social security number of the employee.
        emergency_contact_name (str): Name of the emergency contact person.
        emergency_contact_phone (str): Phone number of the emergency contact person.
        spouse_name (str): Name of the spouse.
        spouse_phone (str): Phone number of the spouse.
        profession_id (int): Foreign key referencing the Profession entity.
        position_id (int): Foreign key referencing the Position entity.
        service_id (int): Foreign key referencing the Service entity.
        department_id (int): Foreign key referencing the Department entity.
        company_id (int): Foreign key referencing the Company entity.
        hire_date (date): Date when the employee was hired.
        leave_date (date): Date when the employee left the company.

    Notes:
        - The matricule,first_name, last_name, profession_id, position_id, company_id, hire_date are required.
        - The first_name, last_name must be 50 characters max.
        - The personal_email, emergency_contact_name and spouse_name must be 100 characters max.
        - The address must be 255 characters max.
        - The social_security_number must be 30 characters max.
        - The personal_phone, emergency_contact_phone and spouse_phone must be 20 characters max.
    """
    matricule: int = Field(..., description="Matricule of the employee.")
    first_name: str = Field(..., max_length=50, description="First name of the employee.")
    last_name: str = Field(..., max_length=50, description="Last name of the employee.")
    birth_date: Optional[date] = Field(None, description="Birth date of the employee.")
    gender: GenderEnum = Field(..., description="Gender of the employee.")
    address: Optional[str] = Field(None, max_length=100, description="Home address of the employee.")
    personal_email: Optional[str] = Field(None, max_length=100, description="Personal email address of the employee.")
    personal_phone: Optional[str] = Field(None, max_length=20, description="Personal phone number of the employee.")
    social_security_number: Optional[str] = Field(None, max_length=30, description="Social security number of the employee.")
    emergency_contact_name: Optional[str] = Field(None, max_length=100, description="Name of the emergency contact person.")
    emergency_contact_phone: Optional[str] = Field(None, max_length=20, description="Phone number of the emergency contact person.")
    spouse_name: Optional[str] = Field(None, max_length=100, description="Name of the spouse.")
    spouse_phone: Optional[str] = Field(None, max_length=20, description="Phone number of the spouse.")
    profession_id: int = Field(..., description="Foreign key referencing the Profession entity.")
    position_id: int = Field(..., description="Foreign key referencing the Position entity.")
    service_id: Optional[int] = Field(None, description="Foreign key referencing the Service entity.")
    department_id: Optional[int] = Field(None, description="Foreign key referencing the Department entity.")
    company_id: int = Field(..., description="Foreign key referencing the Company entity.")
    hire_date: date = Field(..., description="Date when the employee was hired.")
    leave_date: date | None = Field(None, description="Date when the employee left the company.")

class EmployeeCreate(EmployeeBase):
    """
    Schema used for creating a new employee.

    Inherits all fields from EmployeeBase schema.
    """
    pass
    

class EmployeeUpdate(EmployeeBase):
    """
    Schema used when updating an existing employee.

    All fields inherited from EmployeeBase become optional.
    Only fields provided in the request will be updated.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None
    gender: Optional[GenderEnum] = None
    address: Optional[str] = None
    personal_email: Optional[str] = None
    personal_phone: Optional[str] = None
    social_security_number: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    spouse_name: Optional[str] = None
    spouse_phone: Optional[str] = None
    profession_id: Optional[int] = None
    position_id: Optional[int] = None
    service_id: Optional[int] = None
    department_id: Optional[int] = None
    company_id: Optional[int] = None
    hire_date: Optional[date] = None
    leave_date: Optional[date] = None

class EmployeeRead(EmployeeBase):
    """
    Schema used when reading an employee in the database.

    Inherits all fields from EmployeeBase schema.

    Attributes:
        id_employee (int): Unique identifier of the employee.
    """
    id_employee: int

    model_config = ConfigDict(from_attributes=True)