from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from databases.postgresql import Base
from datetime import datetime


class UserAccount(Base):
    """
    Represents a user account stored in the database.

    Attributes:
        id_user (int): Unique identifier of the user account.
        username (str): Unique username (e.g., first letter of first name + last name, like jdoe for John Doe).
        password (str): Encrypted password stored in the database.
        work_email (str): Unique professional email address.
        last_login (datetime): Date and time of the last user login.
        employee_id (int): Foreign key referencing the associated Employee entity.

    Relationship:
        employee (Employee): One-to-One relationship pointing to the
        Employee this account belongs to.
    """

    __tablename__ = "user_accounts"

    id_user: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    work_email: Mapped[str] = mapped_column(String(100), unique=True,nullable=False)
    last_login: Mapped[datetime] = mapped_column(DateTime)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey("employees.id_employee"),unique=True, nullable=False)

    employee = relationship("Employee", back_populates="user_account", uselist=False)