from issues_service.application import services
from classic.components import component

from .join_points import join_point
from falcon import Request, Response


@component
class IssuesController:
    issue_controller: services.IssueService
    #
    # @join_point
    # def on_post_add_issue(self, request: Request, response: Response):
    #     self.issue_controller.add_book(**request.media)
    #     response.media = {'message': 'issue added'}
    #
    # @join_point
    # def on_post_delete(self, request: Request, response: Response):
    #     self.issue_controller.delete_book(**request.media)
    #     response.media = {'message': 'issue deleted'}

    @join_point
    def on_get_get_all_issues(self, request: Request, response: Response):
        issues = self.issue_controller.get_all()
        response.media = {'message': [{
            'issue id': issue.issue_id,
            'api': issue.api,
            'api id': issue.api_id,
            'action': issue.action
        } for issue in issues]}
