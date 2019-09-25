from enum import Enum
from typing import List
import functools


login_user = {}


class Role(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    ANALYST = "analyst"


class User:
    pass


class RequestUser:
    def check_authority(self, user: User) -> bool:
        return True


class LoginUserRepository:
    @staticmethod
    def get():
        return {"name": "admin", "age": 22}


def except_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper


def authority(allowed_roles):
    def _authority(func):
        def wrapper(*args, **kwargs):
            global login_user
            login_user = LoginUserRepository.get()
            if login_user['name'] not in allowed_roles:
                raise Exception("Auth Error.")
            func(*args, **kwargs)
        return wrapper
    return _authority


@except_handler
@authority(allowed_roles=[Role.ADMIN.value, Role.MANAGER.value])
def get():
    print("get")
    print(login_user)


@except_handler
@authority(allowed_roles=[Role.ANALYST.value, Role.MANAGER.value])
def post():
    print("post")
    print(login_user)

    user = User()
    request_user = RequestUser()
    if request_user.check_authority(user) is False:
        raise Exception()


get()
post()

