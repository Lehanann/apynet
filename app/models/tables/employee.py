import uuid
from enum import Enum
from sqlalchemy import Integer, String, Date, CheckConstraint, ForeignKey, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base
from datetime import date
from sqlalchemy.dialects.postgresql import ENUM
from app.utils.gender_enum import GenderEnum
from sqlalchemy.dialects.postgresql import UUID

class Employee(Base):
    """
    Represents an employee stored on the database.

    Attributes:
        id_employee (int): Unique identifier of the employee.
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
        archived (bool): Indicates whether the employee is archived.
    """
    __tablename__ = "employees"

    id_employee: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    matricule: Mapped[int] = mapped_column(Integer,unique=True, nullable=False, index=True)
    document_token: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        default=uuid.uuid4(),
        nullable=False, 
        unique=True
        )
    first_name: Mapped[str] = mapped_column(String(50),nullable=False) 
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    birth_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    gender: Mapped[GenderEnum] = mapped_column(
        ENUM(GenderEnum, name="gender_enum", create_type=False), 
        nullable=False, 
        server_default=text("'x'")
        )
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)
    personal_email: Mapped[str | None] = mapped_column(String(100), unique=True, nullable=True)
    personal_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    social_security_number: Mapped[str | None] = mapped_column(String(30), unique=True, nullable=True)
    emergency_contact_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    emergency_contact_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    spouse_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    spouse_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    profession_id: Mapped[int] = mapped_column(Integer, ForeignKey("professions.id_profession"), nullable=False)
    position_id: Mapped[int] = mapped_column(Integer, ForeignKey("positions.id_position"), nullable=False) 
    service_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("services.id_service"), nullable=True) 
    department_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("departments.id_department"), nullable=True) 
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id_company"), nullable=False)
    hire_date: Mapped[date] = mapped_column(Date, server_default=text("CURRENT_DATE"))
    leave_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    archived: Mapped[bool] = mapped_column(Boolean, default=False, server_default=text("false"), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "personal_phone ~ '^[0-9+ ]*$'",
            name="chk_employee_phone",
            ),
        )
    
    user_account = relationship("UserAccount", back_populates="employee", uselist=False)