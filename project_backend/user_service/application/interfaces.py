from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import User
from .services import UserUpdate

class UsersRepo(ABC):
    @abstractmethod
    def add(self, user:User):
        pass

    @abstractmethod
    def get_or_create(self, user:User):
        pass

    @abstractmethod
    def get_by_id(self, id_:int):
        pass

    @abstractmethod
    def delete(self, user_id:int):
        pass

    @abstractmethod
    def update(self, user:UserUpdate):
        pass
