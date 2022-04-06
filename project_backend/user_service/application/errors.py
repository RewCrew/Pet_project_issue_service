from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = "no user exist "
    code = 'user.not_member'


class NoChat(AppError):
    msg_template = "No chat with id '{chat_id}' exist"
    code = 'chat.no_chat'


class NotCreator(AppError):
    msg_template = "user with id '{user_id}' not a creator of chat"
    code = 'chat.not_creator'
