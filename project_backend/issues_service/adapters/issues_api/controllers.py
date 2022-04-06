from book_service.application import services
from classic.components import component

from .join_points import join_point
from falcon import Request, Response



@component
class IssuesController:
    issue_controller: services.IssueService

    @join_point
    def on_post_add_book(self, request: Request, response: Response):
        self.issue_controller.add_book(**request.media)
        response.media = {'message': 'book added'}

    #
    @join_point
    def on_post_update(self, request: Request, response: Response):
        self.issue_controller.update(**request.media)
        response.media = {'message': 'book updated'}

    @join_point
    def on_post_delete(self, request: Request, response: Response):
        self.issue_controller.delete_book(**request.media)
        response.media = {'message': 'book deleted from library'}


    @join_point
    def on_post_take_book(self, request: Request, response: Response):
        request.media['owner_id'] = request.context.client.user_id

        self.issue_controller.take_book(**request.media)
        response.media = {'message': 'book taken by you'}

    @join_point
    def on_post_return_book(self, request: Request, response: Response):
        request.media['owner_id'] = request.context.client.user_id
        self.issue_controller.return_book(**request.media)
        response.media = {'message': 'book returned'}

    @join_point
    def on_get_get_all_books(self, request: Request, response: Response):
        books = self.issue_controller.get_all()
        response.media = {'library': [{
            'book id': book.book_id,
            'title': book.book_title,
            'author': book.author_name,
            'current owner': book.owner_id
        } for book in books]}


    @join_point
    def on_get_get_user_books(self, request: Request, response: Response):
        owner_id = int(request.context.client.user_id)
        books = self.issue_controller.get_user_books(owner_id)
        response.media = {f'user {request.context.client.user_id} books': [{
            'book id': book.book_id,
            'title': book.book_title,
            'author': book.author_name,
            'current owner': book.owner_id
        } for book in books]}

    @join_point
    def on_get_get_free_books(self, request: Request, response: Response):
        books = self.issue_controller.get_free_books()
        response.media = {f'user {request.context.client.user_id} books': [{
            'book id': book.book_id,
            'title': book.book_title,
            'author': book.author_name
        } for book in books]}
