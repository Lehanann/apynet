from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from databases.postgresql import get_session
from app.logic.user_account_service import UserAccountService
from app.schemas.user_account_schema import UserAccountCreate, UserAccountRead, UserAccountUpdate
from app.repositories.user_account_repository import UserAccountRepository

router = APIRouter(prefix="/user-accounts", tags=["user-accounts"])

def get_user_account_service(db: AsyncSession = Depends(get_session)) -> UserAccountService:
    return UserAccountService(UserAccountRepository(db), db)

@router.get("/",response_model=list[UserAccountRead])
async def list_user_accounts(service: UserAccountService = Depends(get_user_account_service)):
    """
    Retrieve a list of all user_accounts from the database.

    This endpoint fetches all user_accounts stored in the database and returns 
    them in the format specified by the `UserAccountRead` schema.

    Args:
        service (UserAccountService, optional): The service layer for handling
            user_account-related operations. This is injected automatically using
            `Depends(get_user_account_service)`.

    Returns:
        List[UserAccountRead]: A list of user_accounts represented by the `UserAccountRead`
            schema, which includes relevant user_account details such as name and ID.
    """
    return await service.get_all()

@router.get("/{user_account_id}", response_model=UserAccountRead)
async def get_user_account(user_account_id: int, service: UserAccountService = Depends(get_user_account_service)) -> UserAccountRead:
    """
    Retrieve user_account by its ID from the database.

    This endpoint fetches a user_account by its ID stored in the database and returns 
    them in the format specified by the `UserAccountRead` schema.

    Args:
        user_account_id (int): Unique identifier of th euser_account
        Args:
        service (UserAccountService, optional): The service layer for handling
            user_account-related operations. This is injected automatically using
            `Depends(get_user_account_service)`.

    Returns:
        user_account (UserAccountRead): A user_account represented by the `UserAccountRead`
            schema, which includes relevant user_account details such as name and ID.
    """
    
    return await service.get_by_id(user_account_id)
    
"""@router.get("/user_account/{user_account_name}", response_model=UserAccountRead)
async def get_user_account_by_name(user_account_name: str, service: UserAccountService = Depends(get_user_account_service)):
    service = UserAccountService(db)
    return await service.get_user_account_by_name(user_account_name)"""

@router.post("/", response_model=dict[str,str], status_code=status.HTTP_201_CREATED)
async def create_user_account(data: UserAccountCreate, service: UserAccountService = Depends(get_user_account_service)) -> dict[str,str]:
    """
    Create a new user_account.

    Args:
        data (UserAccountCreate): The datas used to create the user_account.
        service (UserAccountService, optional): The service layer for handling
            user_account-related operations. This is injected automatically using
            `Depends(get_user_account_service)`.

    Raises:
        HTTPException: If the user_account creation fails or if the user_account name already exists.

    Returns:
        dict[str,str]: A dictionary containing a success message if the user_account was created successfully.
    """
    await service.create(data)
    return {"message": "UserAccount created successfully!"}
   
@router.put("/{user_account_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
@router.patch("/{user_account_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def update_user_account(user_account_id: int, data: UserAccountUpdate, service: UserAccountService = Depends(get_user_account_service)) -> dict[str,str]:
    """
    Update a user_account by its ID.

    Args:
        user_account_id (int): Unique identifier of the user_account.
        data (UserAccountUpdate): The data used to update the user_account.
        service (UserAccountService, optional): The service layer for handling
            user_account-related operations. This is injected automatically using
            `Depends(get_user_account_service)`.

    Raises:
        HTTPException: if the name already exist or if the user_account is not found by its ID.

    Returns:
        dict[str,str]: A dictionary containing a success message if the user_account was updated successfully.
    """
    
    await service.update(user_account_id, data)
    return {"message": "the user_account updated successfully."}
    
@router.delete("/{user_account_id}", response_model=dict[str,str], status_code=status.HTTP_200_OK)
async def delete_user_account(user_account_id: int, service: UserAccountService = Depends(get_user_account_service)) -> dict[str,str]:
    """
    Delete a user_account by its ID.

    Args:
        user_account_id (int): Unique identifier of the user_account.
        service (UserAccountService, optional): The service layer for handling
            user_account-related operations. This is injected automatically using
            `Depends(get_user_account_service)`.

    Raises:
        HTTPException: if the user_account with the specified ID is not found.
    Returns:
        dict[str,str]: A dictionary containing a success message if the user_account was deleted successfully.
    """

    await service.delete(user_account_id)
    return {"message": "the user_account deleted successfully."}
