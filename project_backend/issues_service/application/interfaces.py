from abc import ABC, abstractmethod
from .dataclasses import Issue


class IssuesRepo(ABC):
    @abstractmethod
    def add(self, issue: Issue):
        pass

    @abstractmethod
    def get_or_create(self, issue: Issue):
        pass

    @abstractmethod
    def get_by_id(self, id_: int):
        pass

    @abstractmethod
    def delete(self, book_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass
