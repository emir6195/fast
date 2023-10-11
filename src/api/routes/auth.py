from fastapi import APIRouter, Depends
from lib.auth import auth_ops, JWTBearer
from lib.user import user_ops
from models.user import UserModel

router = APIRouter()


@router.post("/login", tags=["authorization"])
async def login(user: UserModel):
    response = {
        "err": False,
        "message": "User logged in successfully",
        "token": None
    }
    ins_user = user_ops.get_user(user)
    if (ins_user):
        is_password_valid = auth_ops.checkPassword(
            user.password, ins_user.password)
        if (is_password_valid):
            token = auth_ops.generate_token({"username": user.username})
            response["token"] = token
        else:
            response["err"] = True
            response["message"] = "Password is wrong!"
    else:
        response["err"] = True
        response["message"] = "User not found!"
    return response


@router.get("/validate",dependencies=[Depends(JWTBearer())],  tags=["authorization"] )
def validate():
    return {"success": True}