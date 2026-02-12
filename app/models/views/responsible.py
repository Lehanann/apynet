from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy import String, Integer, Date
from databases.postgresql import Base


class DepartmentResponsible(Base):
    __tablename__ = "v_department_responsibles"
    __table_args__ = {"schema": "intranet"}

    id_department: Mapped[int] = mapped_column(primary_key=True)
    id_employee: Mapped[int] = mapped_column(primary_key=True)

    department_name: Mapped[str] = mapped_column(String)
    company_name: Mapped[str] = mapped_column(String)
    corporate_name: Mapped[str] = mapped_column(String)

    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    work_email: Mapped[str | None] = mapped_column(String)
    personal_phone: Mapped[str | None] = mapped_column(String)

    profession_name: Mapped[str] = mapped_column(String)
    position_name: Mapped[str] = mapped_column(String)
    hire_date: Mapped[date] = mapped_column(Date)


class ServiceResponsible(Base):
    __tablename__ = "v_service_responsibles"
    __table_args__ = {"schema": "intranet"}

    id_service: Mapped[int] = mapped_column(primary_key=True)
    id_employee: Mapped[int] = mapped_column(primary_key=True)

    service_name: Mapped[str]
    department_name: Mapped[str]
    company_name: Mapped[str]
    corporate_name: Mapped[str]

    first_name: Mapped[str]
    last_name: Mapped[str]
    work_email: Mapped[str | None]
    personal_phone: Mapped[str | None]

    profession_name: Mapped[str]
    position_name: Mapped[str]
    hire_date: Mapped[date]


class StructureResponsible(Base):
    __tablename__ = "v_structure_responsibles"
    __table_args__ = {"schema": "intranet"}

    structure_type: Mapped[str] = mapped_column(primary_key=True)
    structure_id: Mapped[int] = mapped_column(primary_key=True)
    id_employee: Mapped[int] = mapped_column(primary_key=True)

    structure_name: Mapped[str]
    company_name: Mapped[str]
    corporate_name: Mapped[str]

    first_name: Mapped[str]
    last_name: Mapped[str]
    work_email: Mapped[str | None]
    personal_phone: Mapped[str | None]

    profession_name: Mapped[str]
    position_name: Mapped[str]
    hire_date: Mapped[date]
