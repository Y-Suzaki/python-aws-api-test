import boto3
from boto3.dynamodb.conditions import Key
from typing import List

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


class UserRequest:
    def __init__(self):
        self.content = {}

    @property
    def name(self):
        return self.content['name']


class User:
    def __init__(self):
        self.content = {}

    def __str__(self):
        return str(self.content)

    @property
    def email(self):
        return self.content['email']


class RequestNotification:
    def __init__(self, request: UserRequest, approval_users: List[User]):
        self.content = {
            'request': request,
            'approval_users': approval_users,
            'reference_url': 'https://example.com'
        }

    @property
    def to_addresses(self) -> List[str]:
        return [x.email for x in self.content['approval_users']]

    @property
    def subject(self):
        return '承認申請'

    @property
    def message(self):
        name = self.content['request'].name
        url = self.content['reference_url']
        return f'{name}から申請がありました。\n{url}を確認してください。'


class DynamoDbRepository:
    @staticmethod
    def _to_domain(item: dict):
        user = User()
        user.content.update(item)
        return user

    @staticmethod
    def _is_match_role(role: str, item: dict):
        return role in list(map(lambda x: x, item['roles'].keys()))

    @staticmethod
    def _is_match_role_and_uri(role: str, uri: str, item: dict):
        roles = list(filter(lambda x: x[0] == role, item['roles'].items()))
        if roles:
            return uri in roles[0][1]
        return False

    @staticmethod
    def get_list_by_role(role: str) -> List[User]:
        table = dynamodb.Table('User')
        items = table.scan()['Items']
        users = list(map(
            lambda item: DynamoDbRepository._to_domain(item),
            list(filter(lambda item: DynamoDbRepository._is_match_role(role, item), items))))
        return users

    @staticmethod
    def get_by_role_and_uri(role: str, uri: str) -> User:
        table = dynamodb.Table('User')
        items = table.scan()['Items']
        users = list(map(
            lambda item: DynamoDbRepository._to_domain(item),
            list(filter(lambda item: DynamoDbRepository._is_match_role_and_uri(role, uri, item), items))))
        return users[0] if users else None

    @staticmethod
    def get_by_email(email: str) -> User:
        table = dynamodb.Table('User')
        items = table.query(IndexName='index-email', KeyConditionExpression=Key('email').eq(email))['Items']
        return DynamoDbRepository._to_domain(items[0]) if items else None


# DAdmin
admin_request = UserRequest()
admin_request.content['name'] = 'Hayashi ishiro'
admin_users = DynamoDbRepository.get_list_by_role('DataLakeAdministrator')

notification = RequestNotification(admin_request, admin_users)
print(notification.to_addresses)
print(notification.subject)
print(notification.message)
