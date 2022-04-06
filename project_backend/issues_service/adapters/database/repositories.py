from typing import List, Optional

from sqlalchemy import select, desc, delete

from classic.components import component
from classic.sql_storage import BaseRepository

from issues_service.application import interfaces
from issues_service.application.dataclasses import Issue
from issues_service.application import errors


@component
class IssuesRepo(BaseRepository, interfaces.IssuesRepo):
    def add(self, issue: Issue):
        self.session.add(issue)
        self.session.flush()
        self.session.refresh(issue)
        return issue

    def get_by_id(self, id_: int) -> Optional[Issue]:
        query = select(Issue).where(Issue.issue_id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_or_create(self, issue: Issue) -> Issue:
        if issue.issue_id is None:
            self.add(issue)
        else:
            new_issue = self.get_by_id(issue.issue_id)
            if new_issue is None:
                self.add(issue)
            else:
                issue = new_issue
        return issue

    def delete(self, issue_id: int):
        issue = self.session.query(Issue).filter(Issue.issue_id == issue_id).one_or_none()
        if not issue:
            raise errors.NoIssue(message="no issue to delete")
        self.session.delete(issue)
        self.session.commit()

    def get_all(self):
        issues = self.session.query(Issue).order_by(Issue.issue_id).all()
        return issues
