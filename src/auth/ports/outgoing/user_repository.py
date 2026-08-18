from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str):
        raise NotImplementedError

    @abstractmethod
    def create(self, user):
        raise NotImplementedError
