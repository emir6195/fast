import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


salt = bcrypt.gensalt()
SECRET = "this.is.not.a.secret.at.all.cuz.its.just.a.challange"


class AuthOps:
    def __init__(self) -> None:
        self.secret_key = SECRET

    def hashPassword(self, raw_password: str):
        return bcrypt.hashpw(raw_password.encode('utf-8'), salt)

    def checkPassword(self, raw_password: str, hashed_password: str):
        return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password)

    def generate_token(self, data):
        token = jwt.encode({"data": data, "exp": datetime.utcnow(
        ) + timedelta(hours=24)}, self.secret_key, algorithm='HS256')
        return token

    def validate_jwt(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except Exception as e:
            print(e)
            return False


auth_ops = AuthOps()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = auth_ops.validate_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
