from sqlalchemy import Integer, String, Text, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base

class SystemRole(Base):
    """
    Represents a system role stored in the database.

    Attibutes:
        id_system_role (int): Unique identifier of the system role.
        name (str): Name of the system role.
        description (text): Description of the system role.
        permission_level (smallint): permission level of the system role.
    """

    __tablename__ = "system_roles"

    id_system_role: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    permission_level: Mapped[int] = mapped_column(SmallInteger, nullable=False, server_default="1")
