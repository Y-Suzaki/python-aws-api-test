from abc import ABCMeta, abstractmethod
from typing import List
from base_domain import BaseDomain


class BaseNotification(BaseDomain, metaclass=ABCMeta):
    @property
    @abstractmethod
    def to_addresses(self) -> List[str]:
        pass

    @property
    @abstractmethod
    def subject(self):
        pass

    @property
    @abstractmethod
    def message(self):
        pass
