from book_service.adapters.books_api import controllers, auth
from classic.http_api import App
from classic.http_auth import Authenticator
from book_service.application import services


def create_app(
        is_dev_mode: bool,
        books: services.BookService,
) -> App:
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)

    if is_dev_mode:
        authenticator.set_strategies(auth.jwt_strategy)

    app = App(prefix='/api')

    app.register(controllers.BooksController(book_controller=books, authenticator=authenticator))

    return app
