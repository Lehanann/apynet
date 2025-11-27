from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base


class Company(Base):
    """
    Docstring for Company
    """
    __tablename__ = "companies"

    id_company: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    corporate_id: Mapped[int] = mapped_column(ForeignKey("corporates.id_corporate"), nullable=False)

    # corporate = relationship("Corporate", back_populates="companies")