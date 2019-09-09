from notification.base_notification import BaseNotification
from user.user_request import UserRequest
from user.user import User
from typing import List


class RequestNotification(BaseNotification):
    def __init__(self, request: UserRequest, approval_users: List[User]):
        super().__init__()
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
