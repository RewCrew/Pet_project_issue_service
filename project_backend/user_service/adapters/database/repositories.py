from typing import List, Optional

from sqlalchemy import select, desc, delete

from classic.components import component
from classic.sql_storage import BaseRepository

from user_service.application import interfaces
from user_service.application.dataclasses import User


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):
    def add(self, user: User):
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)
        return user

    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_or_create(self, user: User) -> User:
        if user.id is None:
            self.add(user)
        else:
            new_user = self.get_by_id(user.id)
            if new_user is None:
                self.add(user)
            else:
                user = new_user
        return user

    def delete(self, user_id:int):
        query = delete(User).where(User.id == user_id)
        self.session.execute(query)
        self.session.flush()
