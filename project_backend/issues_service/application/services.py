from application import errors
from pydantic import validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component

from . import interfaces
from .dataclasses import Issue
from issues_service.application import errors

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
    def delete_issue(self, issue_id: int):
        self.issues_repo.delete(issue_id)

    @join_point
    def get_all(self):
        issues = self.issues_repo.get_all()
        return issues


    @join_point
    def get_issue(self, issue_id: int):
        issue = self.issues_repo.get_by_id(issue_id)
        if issue is None:
            raise errors.NoIssue(message="no issue exist")
        else:
            return issue
