import boto3
from boto3.dynamodb.conditions import Key
from typing import List
from user.user import User
from user.user_request import UserRequest
from notification.base_notification import BaseNotification
from notification.request_notification import RequestNotification
from notification.reject_notification import RejectNotification

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


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


class NotificationRepository:
    @staticmethod
    def notify(notification: BaseNotification):
        print(notification.to_addresses)
        print(notification.subject)
        print(notification.message)


# DAdmin
admin_request = UserRequest()
admin_request.content['name'] = 'Hayashi ishiro'
admin_request.content['email'] = 'hayashi@gmail.com'
admin_request.content['remarks'] = '事前に確認する情報が足りていません。'
admin_users = DynamoDbRepository.get_list_by_role('DataLakeAdministrator')

# approve
NotificationRepository.notify(RequestNotification(admin_request, admin_users))

# reject
NotificationRepository.notify(RejectNotification(admin_request))
