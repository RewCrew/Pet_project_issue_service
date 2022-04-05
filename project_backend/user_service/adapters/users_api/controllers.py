from user_service.application import services
from classic.components import component

from .join_points import join_point
from falcon import Request, Response

from classic.http_auth import (
    authenticate,
    authenticator_needed,

)


@authenticator_needed
@component
class Users:
    users: services.UsersService

    @join_point
    def on_post_register(self, request: Request, response: Response):
        token = self.users.add_user(**request.media)
        response.media = {
            "Users complete, your token is - ": token
        }

    @authenticate
    @join_point
    def on_post_delete_user(self, requset: Request, response: Response):
        # requset.media['user_id'] = requset.context.client.user_id
        self.users.delete_user(requset.context.client.user_id)
        response.media = {'message': 'you are deleted from library'}

    @authenticate
    @join_point
    def on_post_update(self, requset: Request, response: Response):
        requset.media['id'] = requset.context.client.user_id
        self.users.update_user(**requset.media)
        response.media = {'message': 'user updated'}
