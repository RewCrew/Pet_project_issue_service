from classic.app.errors import AppError


class NoIssue(AppError):
    msg_template = "issue with id '{issue.issue_id}' doesnt exist"
    code = 'issue.no_issue'


class NoBook:
    pass
