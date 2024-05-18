import users.crud as crud
import users.schemas as schemas
import users.exceptions as exceptions
from dependecies import session
from database import DBSession

from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/user/register", response_model=schemas.Response)
async def UserRegistration(user: schemas.CreateUser, db: DBSession = Depends(session)):
    if crud.find_user(db, user.login):
        raise exceptions.BusyLogin()
    new_user = crud.create_user(db, user)
    result = schemas.Response(success=True, accessToken=new_user.accessToken)
    return result
