from enum import Enum
from typing import List


class UserRole:
    @property
    def id(self):
        return "001"

    @property
    def name(self):
        return "Admin"

    @property
    def uri(self):
        return "uri1"


class Role(Enum):
    ADMIN = 'Admin'
    MANAGER = 'Manager'
    DATA_ANALYST = 'DataAnalyst'


class User:
    def __init__(self):
        self.content = {}
        self.content['roles'] = [
            {
                'name': 'Admin',
                'uris': ['uri1']
            },
            {
                'name': 'Manager',
                'uris': ['uri0', 'uri1']
            },
            {
                'name': 'DataAnalyst',
                'uris': ['uri0']
            }
        ]

    def delete_role(self, user_role: UserRole):
        updated_roles = []
        for role in self.content['roles']:
            if role['name'] == user_role.name:
                deleted_uris = [uri for uri in role['uris'] if uri != user_role.uri]
                if deleted_uris or user_role.name == Role.ADMIN.value or user_role.name == Role.MANAGER:
                    updated_roles.append({'name': role['name'], 'uris': deleted_uris})
            else:
                updated_roles.append({'name': role['name'], 'uris': role['uris']})
        self.content['roles'] = updated_roles





user = User()
user_role = UserRole()

print(user.content)
user.delete_role(user_role)
print(user.content)

