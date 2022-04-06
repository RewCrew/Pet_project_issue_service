from classic.app.errors import AppError


class NoIssue(AppError):
    msg_template = "issue with id '{issue.issue_id}' doesnt exist"
    code = 'issue.no_issue'


class NoChat(AppError):
    msg_template = "No chat with id '{chat_id}' exist"
    code = 'chat.no_chat'


class NotCreator(AppError):
    msg_template = "user with id '{user_id}' not a creator of chat"
    code = 'chat.not_creator'

