import pytest
from unittest.mock import Mock
import datetime

from classic.messaging import Publisher
from issues_service.application import interfaces, dataclasses


@pytest.fixture(scope='function')
def issue():
    return dataclasses.Issue(
        issue_id = 1,
        action='create',
        api='User',
        api_id=1
    )




@pytest.fixture(scope='function')
def issues_repo(issue):
    issues_repo = Mock(interfaces.IssuesRepo)
    issues_repo.get_or_create = Mock(return_value=issue)
    issues_repo.get_by_id = Mock(return_value=issue)
    return issues_repo

@pytest.fixture(scope='function')
def issue_publisher():
    issue_publisher=Mock(Publisher)
    issue_publisher.plan=Mock(return_value=None)
    return issue_publisher


