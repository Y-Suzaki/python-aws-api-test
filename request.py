from enum import Enum
from typing import List


class RequestFlow:
    pass


class RequestLogType:
    pass


class RequestLogTypes:
    pass


class User:
    @property
    def id(self):
        return ""


class Users:
    @property
    def ids(self):
        return []


class UserRepository:
    @staticmethod
    def get_list_by_authentication_user(authentication_user: str) -> Users:
        pass


class RequestRepository:
    @staticmethod
    def create():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def get(id: str):
        pass

    @staticmethod
    def get_list():
        pass

    @staticmethod
    def get_list_by_requesting_users(requesting_users: List[str]):
        pass


class RequestAction(Enum):
    new = "new"
    modify = "modify"
    delete = "delete"

