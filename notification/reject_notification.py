from user.user_request import UserRequest
from notification.base_notification import BaseNotification
from typing import List


class RejectNotification(BaseNotification):
    def __init__(self, request: UserRequest):
        super().__init__()
        self.content = {
            'request': request,
            'reference_url': 'https://example.com'
        }

    @property
    def to_addresses(self) -> List[str]:
        return [self.content['request'].email]

    @property
    def subject(self):
        return '申請却下'

    @property
    def message(self):
        url = self.content['reference_url']
        remarks = self.content['request'].remarks
        return f'申請が却下されました。\n却下理由：{remarks}\n{url}を確認してください。'
