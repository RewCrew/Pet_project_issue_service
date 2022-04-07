import datetime

import pytest
from attr import asdict
from issues_service.application import services, errors


@pytest.fixture(scope='function')
def issue_test(issues_repo):
    return services.IssueService(issues_repo=issues_repo)




test_data_issue = {
    'issue_id': 1,
    'action': 'create',
    'api': 'User',
    'api_id': 1
}


def test_add_issue(issue_test):
    issue_test.add_issue(**test_data_issue)
    issue_test.issues_repo.add.assert_called_once()
    issue = issue_test.get_issue(test_data_issue['issue_id'])
    assert asdict(issue) == test_data_issue


def test_get_issues(issue_test):
    issue = issue_test.get_issue(test_data_issue['issue_id'])
    assert asdict(issue)==test_data_issue

def test_get_wrong_issue(issue_test):
    with pytest.raises(errors.NoIssue):
        issue_test.get_issue(5)


