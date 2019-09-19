from enum import Enum
from typing import List



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


class LoginUserRepository:
    @staticmethod
    def get(id):
        return User()


class RequestRepository:
    @staticmethod
    def create():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def get(id: str):
        return RequestLogType()

    @staticmethod
    def get_list():
        return RequestLogTypes()

    @staticmethod
    def get_list_by_requesting_users(requesting_users: List[str]):
        return RequestLogTypes()


class RequestAction(Enum):
    new = "new"
    modify = "modify"
    delete = "delete"


class RequestFlow:
    @staticmethod
    def get(id):
        request = RequestRepository.get(id)
        return request

    @staticmethod
    def get_list():
        login_user = LoginUserRepository.get("")
        if login_user:
            requests = RequestRepository.get_list()
        else:
            users = UserRepository.get_list_by_authentication_user(login_user.id)
            requests = RequestRepository.get_list_by_requesting_users(users.ids)
        return requests
