from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from book_service.adapters import database, books_api
from book_service.application import services


class Settings:
    db = database.Settings()
    books_api = books_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    books_repo = database.repositories.BooksRepo(context=context)
    # chats_repo = database.repositories.ChatsRepo(context=context)
    # chat_users_repo = database.repositories.ChatUsersRepo(context=context)
    # messages_repo = database.repositories.MessagesRepo(context=context)


class Application:
    book_controller = services.IssueService(books_repo=DB.books_repo)
    is_dev_mode = Settings.books_api.IS_DEV_MODE


class Aspects:
    services.join_points.join(DB.context)
    books_api.join_points.join(DB.context)


app = books_api.create_app(
    books = Application.book_controller,
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
