from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from databases.postgresql import Base

class Department(Base):

    __tablename__ = "departments"

    id_department: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id_company") ,nullable=False)