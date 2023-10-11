from pydantic import BaseModel, Field
from datetime import datetime

class UserModel(BaseModel):
    username: str
    password: str
    role: str = Field(default="default")