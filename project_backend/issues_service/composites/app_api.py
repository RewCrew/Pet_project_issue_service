from threading import Thread

from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from issues_service.adapters import database, issues_api, message_bus
from issues_service.application import services
from kombu import Connection


class Settings:
    db = database.Settings()
    issues_api = issues_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = database.repositories.IssuesRepo(context=context)


class Application:
    issues_controller = services.IssueService(issues_repo=DB.issues_repo)
    is_dev_mode = Settings.issues_api.IS_DEV_MODE


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    consumer = message_bus.create_consumer(connection, Application.issues_controller)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


class Aspects:
    services.join_points.join(DB.context)
    issues_api.join_points.join(DB.context)


MessageBus.declare_scheme()
consumer = Thread(target=MessageBus.consumer.run, daemon=True)
consumer.start()

app = issues_api.create_app(
    issues=Application.issues_controller,
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
