from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from issues_service.adapters import database, issues_api
from issues_service.application import services


class Settings:
    db = database.Settings()
    issues_api = issues_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = database.repositories.IssuesRepo(context=context)
    # chats_repo = database.repositories.ChatsRepo(context=context)
    # chat_users_repo = database.repositories.ChatUsersRepo(context=context)
    # messages_repo = database.repositories.MessagesRepo(context=context)


class Application:
    issues_controller = services.IssueService(issues_repo=DB.issues_repo)
    is_dev_mode = Settings.issues_api.IS_DEV_MODE


class Aspects:
    services.join_points.join(DB.context)
    issues_api.join_points.join(DB.context)


app = issues_api.create_app(
    issues = Application.issues_controller,
    is_dev_mode=Application.is_dev_mode
)

if __name__ == "__main__":
    from wsgiref import simple_server

    with simple_server.make_server('', 8000, app=app) as server:
        server.serve_forever()

        # hupper - m
        # waitress - -port = 8000 - -host = 127.0
        # .0
        # .1
        # user_service.composites.users_api: app
