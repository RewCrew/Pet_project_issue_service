from typing import List, Optional, Tuple

import jwt
from application import errors
from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component

from . import interfaces
from .dataclasses import Issue

join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    action: str
    api: str
    api_id: int


@component
class IssueService:
    issues_repo: interfaces.IssuesRepo

    @join_point
    @validate_with_dto
    def add_issue(self, issues_info: IssueInfo):
        issue = issues_info.create_obj(Issue)
        self.issues_repo.add(issue)


    @join_point
    @validate_arguments
    def delete_book(self, book_id: int):
        self.issues_repo.delete(book_id)

    @join_point
    def get_all(self):
        books = self.issues_repo.get_all()
        return books


    @join_point
    def get_book(self, book_id: int):
        book = self.issues_repo.get_by_id(book_id)
        if book is None:
            raise errors.NoBook(message="No book exist")
        else:
            return book
