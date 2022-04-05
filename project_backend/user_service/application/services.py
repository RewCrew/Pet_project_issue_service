from typing import List, Optional, Tuple

import jwt
from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component

from . import interfaces, errors
from .dataclasses import User

join_points = PointCut()
join_point = join_points.join_point


#
class UserInfo(DTO):
    name: str
    email: str


class UserUpdate(DTO):
    name: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None


@component
class UsersService:
    user_repo: interfaces.UsersRepo

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        new_user = user_info.create_obj(User)
        user = self.user_repo.get_or_create(new_user)
        token = jwt.encode(
            {"sub": user.id,
             "name": user.name,
             "email": user.email,
             "login": user.name,
             "group": "User"}
            , 'kerim_project', algorithm='HS256')
        return token

    @join_point
    @validate_arguments
    def delete_user(self, user_id:int):
        self.user_repo.delete(user_id)

    @join_point
    @validate_with_dto
    def update_user(self, user: UserUpdate):
        self.user_repo.update(user)

