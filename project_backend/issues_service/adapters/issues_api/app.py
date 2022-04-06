import falcon

from . import controllers, auth
from classic.http_api import App
from classic.http_auth import Authenticator
from issues_service.application import services


def create_app(
        is_dev_mode: bool,
        issues: services.IssueService,
) -> App:
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)

    if is_dev_mode:
        authenticator.set_strategies(auth.jwt_strategy)

    app = App(prefix='/api')

    app.register(controllers.IssuesController(issue_controller=issues, authenticator=authenticator))

    return app
