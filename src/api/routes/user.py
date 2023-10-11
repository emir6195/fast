from fastapi import APIRouter, Depends
from models.user import UserModel
from lib.user import user_ops
from lib.auth import JWTBearer

router = APIRouter()


@router.get("/",  dependencies=[Depends(JWTBearer())], tags=["user"])
async def getAllUsers():
    users = user_ops.get_all_users()
    return users

@router.post("/create_admin", tags=["user"])
async def create_admin(user: UserModel):
    user.role = "SUPER_USER"
    user_ops.create_user(user)
    return user


@router.post("/create_user", dependencies=[Depends(JWTBearer())], tags=["user"])
async def create_user(user: UserModel): 
    user_ops.create_user(user)
    return user