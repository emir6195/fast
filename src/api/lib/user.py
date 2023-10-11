from database import db_ops
from database import User
from models.user import UserModel
from lib.auth import auth_ops


class UserOps:
    def __init__(self) -> None:
        pass

    def get_user(self, user: UserModel):
        session = db_ops.create_db_session()
        user_record = session.query(User).filter_by(
            username=user.username).first()
        session.close()
        return user_record

    def create_user(self, user: UserModel) -> None:
        if user.role == "SUPER_USER" and self.check_if_super_user_exists():
            raise Exception(
                "Super user already exists. Cannot create new one!.")
        else:
            session = db_ops.create_db_session()
            super_user = User(
                username=user.username,
                password=auth_ops.hashPassword(user.password),
                role=user.role,
            )
            session.add(super_user)
            session.commit()
            session.close()

    def get_all_users(self):
        session = db_ops.create_db_session()
        users = session.query(User).all()
        session.close()
        return users

    def check_if_super_user_exists(self):
        session = db_ops.create_db_session()
        user = session.query(User).filter_by(role="SUPER_USER").first()
        session.close()
        return user != None

user_ops = UserOps()