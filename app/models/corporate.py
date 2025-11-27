from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from databases.postgresql import Base

class Corporate(Base):
    """
    Docstring for Corporate
    Model corporate containing all Fields of corporates table
    """
    __tablename__ = "corporates"

    id_corporate: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
